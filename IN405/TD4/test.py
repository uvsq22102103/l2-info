import os
from pwd import getpwuid
from time import gmtime
from datetime import datetime

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


def dir_all_list(path_in):
    """return mode user size last_access_time name"""
    stat = os.stat(path_in)
    mode = 0
    for i, value in enumerate(oct(stat.st_mode)[-3:]):
        mode += int(value)*(8**(2-i))
    mode = mode_octal_to_str(mode)
    user = getpwuid(stat.st_uid).pw_name
    size = str(stat.st_size)
    date = gmtime(stat.st_atime)
    mois = {1:"Jan.",2:"Fev.",3:"Mars",4:"Avril",5:"Mai",6:"Juin",
            7:"Juillet",8:"Août",9:"Sept.",10:"Oct.",11:"Nov.",12:"Dec."}
    last_access_time = str(date.tm_mday)+" "+mois[date.tm_mon]+" "+str(date.tm_year)
    name = os.path.basename(path_in)
    return " ".join([mode,user,size,last_access_time,name])

print(dir_all_list("./"))