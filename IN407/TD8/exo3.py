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


class Definition():
    """Exercice 4"""
    def __init__(self, word:str, meaning:str):
        self.word = CString(word)
        self.meaning = CString(meaning)
    
    def getClef(self):
        return self.word.get_chaine()
    
    def getDef(self):
        return self.meaning.get_chaine()
    
    def __str__(self):
        return f"{self.word} : {self.meaning}"


class Dictionnaire():
    """Contient un ensemble de définitions"""
    def __init__(self, definitions:list[Definition]=[]):
        self.dictionnaire = {}
        for mot in definitions:
            self.dictionnaire[mot.getClef()] = mot.getDef()
    
    def Recherche(self, word:str):
        if word in self.dictionnaire.keys():
            return self.dictionnaire[word]
        else:
            print(f"Le mot {word} n'existe pas dans ce Dictionnaire.")
            raise ValueError
    
    def get_all_Def(self) -> list[Definition]:
        dico = self if type(self) == dict else self.dictionnaire
        output = []
        for (word, meaning) in dico.items():
            output.append(Definition(word, meaning))
        return output
    
    def __add__(self, definition:Definition):
        return Dictionnaire(self.get_all_Def() + [definition])
    
    def __iadd__(self, definition:Definition):
        return self + definition
    
    def __sub__(self, mot:str|Definition):
        dico = self.dictionnaire.copy()
        if type(mot) == str:
            if mot in dico.keys():
                dico.pop(mot)
            return Dictionnaire(Dictionnaire.get_all_Def(dico))
        elif type(mot) == Definition:
            if (cle:=mot.getClef()) in dico.keys():
                dico.pop(cle)
            return Dictionnaire(Dictionnaire.get_all_Def(dico))
    
    def __isub__(self, mot:str|Definition):
        return self - mot
    
    def __str__(self):
        output = ""
        for definition in self.get_all_Def():
            output += definition.__str__()+"\n"
        return output


def1 = Definition("Berger", "Entraîne des moutons pour des combats de MMA")
Larousse = Dictionnaire([def1])
Larousse += Definition("Règle", "Sert à mesurer la taille de sa")
result = Larousse.Recherche("Règle")
print(result)
Larousse -= "Règle"
