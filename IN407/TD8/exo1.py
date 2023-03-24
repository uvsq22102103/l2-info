class CString():
    """Exercice 3"""
    __nbr = 0
    def __init__(self, txt:str=""):
        CString.__nbr += 1
        self.txt = txt
    
    def nbr_Chaines():
        return CString.__nbr
    
    def plus(self,txt):
        self.txt += txt
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
        return f'<content : "{self.get_chaine()}" lenght : {len(self.get_chaine())}>'
    
    def __iadd__(self, pt):
        if type(pt) == CString:
            return self.plus(pt.get_chaine())
        elif type(pt) == str:
            return self.plus(pt)
        else:
            raise TypeError

a = CString("Bonjour ")
b = CString("Thomas")
ab = a+b
print(f'"{a}"+"{b}"="{ab}"')
print(a>b)
print(a<=b)