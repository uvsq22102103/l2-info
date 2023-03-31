class Complexe():
    def __init__(self, reel:int, imaginaire:int) -> None:
        self.reel = reel
        self.imaginaire = imaginaire
    
    def __str__(self) -> str:
        a, b = self.get_value()
        return f"{a} + {b}i"
    
    def __add__(self, cp:"Complexe"):
        a, b = self.get_value()
        c, d = cp.get_value()
        return Complexe(a+c, b+d)
    
    def __iadd__(self, cp:"Complexe"):
        return self + cp
    
    def get_value(self):
        return self.reel, self.imaginaire

    def __mul__(self, cp:"Complexe"):
        """(a + bi) * (c + di) = (ac - bd) + (ad + bc)i"""
        a, b = self.get_value()
        c, d = cp.get_value()
        return Complexe((a*c - b*d), (a*d + b*c))
    
    def __pow__(self, pow:int):
        a, b = self.get_value()
        resultat = Complexe(a, b)
        for _ in range(pow-1):
            resultat = resultat * self
        return resultat


cp1 = Complexe(2, 5)
print(cp1**3)