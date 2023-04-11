from abc import ABCMeta, abstractmethod

class CList(metaclass = ABCMeta):
    def __init__(self) -> None:
        self.values = []
        self.taille = 0
    
    def ajouter(self, value):
        self.taille += 1
        self.values.append(value)
    
    @abstractmethod
    def enlever(self):
        if self.taille > 0:
            self.taille -= 1
        else:
            raise IndexError("C'est vide :(")
    
    def __str__(self) -> str:
        return "La liste comprend les elements suivants : {}".format(self.values)
    
    def get_taille(self):
        return self.taille
    
    @abstractmethod
    def __gt__(self, value):
        """Dépiler"""
        pass

    @abstractmethod
    def __lt__(self, value):
        """Empiler"""
        self.ajouter(value)

class CPile(CList):
    def __init__(self) -> None:
        super().__init__()

    def ajouter(self, value):
        super().ajouter(value)

    def enlever(self):
        super().enlever()
        return self.values.pop()
    
    def __lt__(self, value):
        super().__lt__(value)

    def __gt__(self, value):
        pass

class CFile(CList):
    def __init__(self) -> None:
        super().__init__()
    
    def ajouter(self, value):
        super().ajouter(value)
    
    def enlever(self):
        super().enlever()
        return self.values.pop(0)
    
    def __lt__(self, value):
        super().__lt__(value)
    
    def __gt__(self, value):
        pass