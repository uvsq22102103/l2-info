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
        return len(self.get_chaine()) > len(pt.get_chaine())
    
    def infOuEgale(self, pt):
        return len(self.get_chaine()) <= len(pt.get_chaine())
    
    def plusGrand(self, pt):
        if self.plusGrandeQue(pt):
            return self
        else:
            return pt

class Definition():
    """Exercice 4"""
    def __init__(self, word:str, meaning:str):
        self.word = CString(word)
        self.meaning = CString(meaning)
    
    def getClef(self):
        return self.word.get_chaine()
    
    def getDef(self):
        return self.meaning.get_chaine()
    

################################## EXERCICE 3 #####################################
#s1 = CString("toto")
#s2 = CString("q")
#
#print("Le nombre de chaînes de caractères créées est :", CString.nbr_Chaines())
#
#s3 = s1.plus("w")
#
#print("s3=", s3.get_chaine())
#print("s3=", s3)
#
#if s1.plusGrandeQue(s2):
#    print("s1 est plus grand que s2".format(s1.get_chaine(), s2.get_chaine()))
#
#if s1.infOuEgale(s2):
#    print(f"{0} est plus petit {1}".format(s1.get_chaine(), s2.get_chaine()))
#
#s3 = s1.plusGrand(s2)
################################## EXERCICE 4 #####################################
#homer = Definition("Homer", "Buveur de bière")
#print(f'La definition du mot "{homer.getClef()}" est "{homer.getDef()}"')
###################################################################################
