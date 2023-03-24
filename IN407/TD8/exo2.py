class Vecteur():
    
    def __init__(self, values:list[int]):
        self.values = values

    def set_values(self, value:list[int]):
        self.values = value
    
    def get_values(self):
        return self.values.copy()
    
    def __add__(self, value:int):
        return Vecteur(self.get_values() + [value])
    
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