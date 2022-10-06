class Nombre:
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
        nba = Nombre(self.value,self.base).decimal()
        return Nombre(nba).decimal_to_base(baseb)
    
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
        nb = Nombre.complement_a_un(nb)
        for i in range(x-1):
            nb = Nombre.__complement(nb)
        return nb

    
    def r_entier_signés(self, nb_bits:int = 8):
        bits = Nombre(self.value,self.base).turn_to_baseb(2)
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
            nb = Nombre(int(i)).decimal_to_base(2)
            while len(nb) < 4:
                nb = "0" + nb
            output += nb
        return output

# à faire :  addition et multiplication d'entiers binaire
#            codage des flottants, conversion des flottants, addition et multiplication.


nb = Nombre(-48)
print(nb.decimal())
print(nb.decimal_to_base(2))
print(nb.turn_to_baseb(2))
test = nb.r_entier_signés()
print(test)
print(Nombre.complement_a_un(test))
print(Nombre.complement_a_x(test,2))
print(Nombre.complement_a_x(test,3))
print(nb.BDC())