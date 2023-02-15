#!/usr/bin/python3

import os
import tempfile
import unittest

def file_cat(path_in):
    os.system("cat "+path_in)

def file_copy(path_in, path_out):
    os.system("cp "+path_in+" "+path_out)

def file_move(path_in, path_out):
    os.system("mv "+path_in+" "+path_out)

def file_find(path, filename):
    os.system("find "+path+" -name '"+filename+"'")

def file_diff(path_a, path_b):
    with open(path_a, "r") as f1:
        with open(path_b, "r") as f2:
            return (f1.readlines() == f2.readlines())

def file_sed_char(path, target, modif):
    with open(path, "r") as f:
        text = "".join(f.readlines())
    text = text.replace(target,modif)
    with open(path, "w") as f:
        f.write(text)


def file_sed_string(path, target, modif):
    with open(path, "r") as f:
        text = "".join(f.readlines())
    text = text.replace(target,modif)
    with open(path, "w") as f:
        f.write(text)

def file_grep_char(path_in, target):
    with open(path_in, "r") as f:
        text = "".join(f.readlines())
    r = []
    for i,l in enumerate(text):
        if l == target:
            r.append(i)
    return r

def file_grep_string(path_in, target):
    with open(path_in,"r") as f:
        lines = f.readlines()
    n_line = 0
    r = []
    for line in lines:
        indice = 0
        while indice < len(line)-1:
            try:
                indice = line[indice:].index(target) + indice
                r.append((n_line,indice))
            except ValueError:
                break
            indice += 1
        n_line += 1
    return r

def file_grep_line(path_in, target):
    with open(path_in,"r") as f:
        return target in f.readlines()

class TestBasicFileGrepString(unittest.TestCase):
    def test_empty_file(self):
        tmp_f = tempfile.NamedTemporaryFile()
        tmp_f.flush()

        prev = os.dup(1)
        os.close(1)
        _ = os.open('__buffer__', os.O_CREAT | os.O_WRONLY | os.O_TRUNC)
        file_grep_string(tmp_f.name, 'a')
        os.dup2(prev, 1)

        tmp_f.close()
        with open('__buffer__') as exec_res:
            good_lines = []
            exec_lines = exec_res.readlines()
            self.assertListEqual(good_lines, exec_lines)
        
        os.unlink('__buffer__')

    def test_simple_search(self):
        tmp_f = tempfile.NamedTemporaryFile(mode='w')
        tmp_f.writelines([
            "123\n",
            "abc\n",
            "ABC\n"
        ])
        tmp_f.flush()

        prev = os.dup(1)
        os.close(1)
        _ = os.open('__buffer__', os.O_CREAT | os.O_WRONLY | os.O_TRUNC)
        file_grep_string(tmp_f.name, 'abc')
        os.dup2(prev, 1)

        tmp_f.close()
        with open('__buffer__') as exec_res:
            good_lines = ['1:0\n']
            exec_lines = exec_res.readlines()
            self.assertListEqual(good_lines, exec_lines)
