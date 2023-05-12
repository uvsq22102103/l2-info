class Celsius:

    erreurs = ["{}°C < 273.15°C (le 0 absolu)",
               "La température n'a pas encore été définie"]
    
    def __init__(self, temperature:int=None) -> None:
        self.__temperature = temperature
    
    def __str__(self) -> str:
        return str(self.__temperature)
    
    def fahrenheit(self) -> int:
        return round((self.get_temperature() * (9 / 5)) + 32, 2)
    
    def set_temperature(self, new_temperature:int):
        if new_temperature > -273.15:
            self.__temperature = new_temperature
            print(self.__temperature)
        else:
            raise ValueError(Celsius.erreurs[0].format(new_temperature))
    
    def get_temperature(self):
        print(self.__temperature)
        if self.__temperature == None:
            raise ValueError(Celsius.erreurs[1])
        return self.__temperature
    
    temperature = property(get_temperature, set_temperature)

#
#human = Celsius()
#human.temperature = 37
#print(human.temperature)
#print(human.fahrenheit())
#print(human.__dict__)
#
#
#human = Celsius()
#print(human.get_temperature())
#print(human.fahrenheit())
#human.set_temperature(-300)
#print(human.fahrenheit())
#

human = Celsius(37)
print(human.temperature)
print(human.fahrenheit())
human.temperature = -300
print(human.temperature)
human.temperature = 37
print(human.fahrenheit())
