from typing import Any

class CString():
    """Exercice 3"""
    __nbr = 0
    def __init__(self, txt:str=""):
        CString.__nbr += 1
        self.txt = txt
        self.len = len(txt)
    
    def nbr_Chaines():
        return CString.__nbr
    
    def plus(self,txt):
        self.txt += txt
        self.len += len(txt)
        return self
    
    def get_chaine(self):
        return self.txt
    
    def plusGrandeQue(self, pt):
        """Au sens alphabetique"""
        return self.get_chaine() > pt.get_chaine()
    
    def infOuEgale(self, pt):
        """Au sens alphabetique"""
        return self.get_chaine() <= pt.get_chaine()
    
    def plusGrand(self, pt):
        if self.plusGrandeQue(pt):
            return self
        else:
            return pt
    
    def __add__(self, pt):
        if type(pt) == CString:
            return CString(self.get_chaine() + pt.get_chaine())
        elif type(pt) == str:
            return CString(self.get_chaine() + pt)
        else:
            raise TypeError
    
    def __gt__(self, pt):
        if type(pt) == CString:
            return self.plusGrandeQue(pt)
        elif type(pt) == str:
            return self.plusGrandeQue(CString(pt))
        else:
            raise TypeError

    def __le__(self, pt):
        if type(pt) == CString:
            return self.infOuEgale(pt)
        elif type(pt) == str:
            return self.infOuEgale(CString(pt))
        else:
            raise TypeError

    def __str__(self) -> str:
        return f'<content : "{self.get_chaine()}" lenght : {self.len}>'
    
    def __iadd__(self, pt):
        return self + pt

class Pair:

    def __init__(self, a:Any, b:Any) -> None:
        if type(a) == type(b):
            self.a = a
            self.b = b
        else:
            raise TypeError("Vous devez mettre en argument deux variable de même type")

    def GetMax(self):
        print(self.a if self.a > self.b else self.b)


i, j = 5, 6
l, m = 10.0, 5.0
#
#k = GetMax(i, j)
#n = GetMax(l, m)
#string = GetMax(CString("pignouf"), CString("rer c"))
#
#print("k=", k)
#print("n=", n)
#print("string=", string.get_chaine())
#
myInts = Pair(5, 2)
myFloats = Pair(l, m)
myStrings = Pair("c", "d")
myInts.GetMax()
myFloats.GetMax()
myStrings.GetMax()