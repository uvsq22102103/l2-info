
class Nombre_entier:
    def __init__(self,valeur:int,base:int=10):
        if valeur < 0:
            self.signe = 1
        else:
            self.signe = 0
        self.value = abs(valeur)
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
            if self.signe == 1:
                output *= -1
            return output
    
    def turn_to_baseb(self, baseb:int):
        nba = Nombre_entier(self.value,self.base).decimal()
        return Nombre_entier(nba).decimal_to_base(baseb)
    
    def complement_a_un(nb:str):
        output = ""
        for i in nb[1:]:
            if i == "0":
                output += "1"
            else:
                output += "0"
        return nb[0]+output
    
    def __complement(nb:str):
        output = ""
        c = False
        for i in nb[::-1]:
            if c is False:
                if i == "0" :
                    output += "1"
                    c = True
                else:
                    output += "0"
            else:
                output += i
        return output[::-1]
    
    def complement_a_x(nb:str,x:int = 2):
        nb = Nombre_entier.complement_a_un(nb)
        for i in range(x-1):
            nb = Nombre_entier.__complement(nb)
        return nb

    
    def r_entier_signés(self, nb_bits:int = 8):
        bits = Nombre_entier(self.value,self.base).turn_to_baseb(2)
        if len(bits) > nb_bits:
            print("l'allocation de bits n'est pas suffisante")
        else:
            while len(bits) < nb_bits-1:
                bits = "0" + bits
        bits = str(self.signe) + bits
        return bits
    
    def BDC(self):
        output = ""
        for i in str(self.value):
            nb = Nombre_entier(int(i)).decimal_to_base(2)
            while len(nb) < 4:
                nb = "0" + nb
            output += nb
        return output
    
    def addition_bits(nb1:str,nb2:str):
        total = Nombre_entier(int(nb1),2).decimal() + Nombre_entier(int(nb2),2).decimal()
        return Nombre_entier(total).decimal_to_base(2)
    
    def multiplication_bits(nb1:str,nb2:str):
        total = Nombre_entier(int(nb1),2).decimal() * Nombre_entier(int(nb2),2).decimal()
        return Nombre_entier(total).decimal_to_base(2)


class Nombre_flottant:
    """Base 10 seulement"""
    def __init__(self,nb:str):
        if nb[0] == "-":
            nb = nb[1:]
            self.signe = 1
        else:
            self.signe = 0
        self.value = nb
        nb = nb.split(".")
        self.arrondi = nb[0]
        self.fractionnaire = nb[1]

#à faire :    codage des flottants, conversion des flottants, addition et multiplication.


nb = Nombre_entier(-48)
print(nb.decimal())
print(nb.decimal_to_base(2))
print(nb.turn_to_baseb(2))
test = nb.r_entier_signés()
print(test)
print(Nombre_entier.complement_a_un(test))
print(Nombre_entier.complement_a_x(test,2))
print(Nombre_entier.complement_a_x(test,3))
print(nb.BDC())
print(Nombre_entier.addition_bits("1111","1000"))
print(Nombre_entier.multiplication_bits("1111","1000"))
test = Nombre_flottant("-416244.521656")
print(test.arrondi)
print(test.fractionnaire)