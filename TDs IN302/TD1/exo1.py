class Nombre:
    def __init__(self,valeur:int,base:int=10):
        self.value = valeur
        self.base = base
    
    def decimal_to_base(self,base:int):
        output, nb = "", self.value
        if base <= 10:
            while nb // base > 0:
                output += str(nb % base)
                nb //= base
            output += str(nb % base)
            return output[::-1]
    
    def decimal(self):
        nb, base = str(self.value), self.base
        output = 0
        puissance = len(nb)-1
        if base <= 10:
            for i in nb:
                output += int(i) * (base ** puissance)
                puissance -= 1
            return output
    
    def turn_to_baseb(self, baseb:int):
        nba = Nombre(self.value,self.base).decimal()
        return Nombre(nba).decimal_to_base(baseb)
    
    def complement_a_un(nb:str):
        output = ""
        for i in nb:
            if i == "0":
                output += "1"
            else:
                output += "0"
        return output
    
    def r_entier_signés(nb,bits):
        if len(nb) < bits:
            pass
        else:
            print("Nombre trop grand pour le nombre de bits choisis ! ")

nb = Nombre(48)
print(nb.decimal())
print(nb.decimal_to_base(2))
print(nb.turn_to_baseb(2))