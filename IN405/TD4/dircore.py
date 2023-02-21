#!/usr/bin/python3
import os
import tempfile
import unittest
from pwd import getpwuid
from time import gmtime

def mode_octal_to_str(octal_value:str):
    """Prend un seul octal en argument et rend les 
    permissions associées."""
    output = ""
    while octal_value > 0:
        perm = octal_value % 8
        output += "x" if perm % 2 == 1 else "-"
        perm //= 2
        output += "w" if perm % 2 == 1 else "-"
        perm //= 2
        output += "r" if perm % 2 == 1 else "-"
        octal_value //= 8
    return output[::-1]

def mode_str_to_octal(str_value:str):
    """Prend une chaine de charactères de taille 9 et renvoi
    l'octal associé."""
    output = 0
    if len(str_value) == 9:
        for i, lettre in enumerate(str_value):
            output += 2**i if lettre != "-" else 0
        return output
    else:
        raise ValueError

def change_mode(path_in:str, new_mode:int):
    """Change les droits d'accès d'un fichier"""
    os.chmod(path_in,new_mode)

def touch(path_in):
    """permet de modifier la date de dernier
    accès et modification du fichier path_in par la date courante,
    ou de créer le fichier s'il n'existe pas.
    Se base sur os.utime()"""
    with open(path_in,"a"):
        os.utime(path_in, None)

def dir_list(path_in):
    return os.listdir(path_in)

def dir_all_list(path_in):
    """return mode user size last_access_time name"""
    mois = {1:"Jan.",2:"Fev.",3:"Mars",4:"Avril",5:"Mai",6:"Juin",
            7:"Juillet",8:"Août",9:"Sept.",10:"Oct.",11:"Nov.",12:"Dec."}
    for path in os.listdir(path_in):
        stat = os.stat(path)
        mode = 0
        for i, value in enumerate(oct(stat.st_mode)[-3:]):
            mode += int(value)*(8**(2-i))
        mode = mode_octal_to_str(mode)
        user = getpwuid(stat.st_uid).pw_name
        size = str(stat.st_size)
        date = gmtime(stat.st_atime)
        last_access_time = str(date.tm_mday)+" "+mois[date.tm_mon]+" "+str(date.tm_year)
        name = os.path.basename(path)
        print (" ".join([mode,user,size,last_access_time,name]))

def dir_rec_list(path_in):
    """Equivalent d'un ls -R"""
    paths = os.listdir(path_in)
    for path in paths:
        if os.path.isdir(path_in+"/"+path):
            print(path_in+"/"+path)
            dir_all_list(path_in+"/"+path)

class TestSimpleDirList(unittest.TestCase):
    def test_empty_dir(self):
        with tempfile.TemporaryDirectory() as folder:
            prev = os.dup(1)
            os.close(1)
            _ = os.open('__buffer__', os.O_CREAT | os.O_WRONLY | os.O_TRUNC)
            dir_rec_list(folder)
            os.dup2(prev, 1)

        with open('__buffer__') as exec_res:
            good_lines = []
            exec_lines = exec_res.readlines()
            self.assertListEqual(good_lines, exec_lines)

        os.unlink('__buffer__')

    def test_two_files(self):
        with tempfile.TemporaryDirectory() as folder:
            files = [tempfile.NamedTemporaryFile(dir=folder) for _ in range(2)]
            for file in files:
                file.flush()

            prev = os.dup(1)
            os.close(1)
            _ = os.open('__buffer__', os.O_CREAT | os.O_WRONLY | os.O_TRUNC)
            dir_rec_list(folder)
            os.dup2(prev, 1)

            for file in files:
                file.close()

        with open('__buffer__') as exec_res:
            good_lines = [os.path.basename(file.name) + '\n' for file in files]
            good_lines.sort()
            exec_lines = exec_res.readlines()
            exec_lines.sort()
            self.assertListEqual(good_lines, exec_lines)

        os.unlink('__buffer__')

    def test_two_dirs(self):
        with tempfile.TemporaryDirectory() as folder_A:
            file_A = tempfile.NamedTemporaryFile(dir=folder_A)
            file_A.flush()

            with tempfile.TemporaryDirectory(dir=folder_A) as folder_B:
                file_B = tempfile.NamedTemporaryFile(dir=folder_B)
                file_B.flush()

                prev = os.dup(1)
                os.close(1)
                _ = os.open('__buffer__', os.O_CREAT | os.O_WRONLY | os.O_TRUNC)
                dir_rec_list(folder_A)
                os.dup2(prev, 1)

                file_A.close()
                file_B.close()

        with open('__buffer__') as exec_res:
            fol_base_A = os.path.basename(folder_A)
            fol_base_B = os.path.basename(folder_B)
            good_lines = [
                os.path.basename(file_A.name) + "\n",
                fol_base_B + "\n",
                fol_base_B + "/" + os.path.basename(file_B.name) + "\n"
            ]
            good_lines.sort()
            exec_lines = exec_res.readlines()
            exec_lines.sort()
            self.assertListEqual(good_lines, exec_lines)

        os.unlink('__buffer__')