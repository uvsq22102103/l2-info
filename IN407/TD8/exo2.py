class Vecteur():
    
    def __init__(self, values:list[int]):
        self.values = values

    def set_values(self, value:list[int]):
        self.values = value
    
    def get_values(self):
        return self.values.copy()
    
    def __add__(self, value):
        if type(value) is int:
            return Vecteur(self.get_values() + [value])
        elif type(value) is Vecteur:
            return Vecteur(self.get_values() + value.get_values())
        elif type(value) is list:
            return Vecteur(self.get_values() + value)
        else:
            raise ValueError(f"{type(value)} non géré")
    
    def __str__(self) -> str:
        return str(self.values)
    
    def __sub__(self, value:int):
        values = self.get_values()
        while value in values:
            values.remove(value)
        return Vecteur(values)
    
    def __iadd__(self, value:int):
        return self + value
    
    def __isub__(self, value:int):
        return self - value

a = Vecteur([3,6,1])
b = a + 3
c = a + [4,8,3]
d = a + Vecteur([7,0])
print(a)
print(b)
print(c)
print(d)