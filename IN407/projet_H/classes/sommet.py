class Sommet():

    def __init__(self, etiquette: int, value: int=None):
        self.etiquette = etiquette
        self.value = value

    def set_etiquette(self, new_etiquette):
        self.etiquette = new_etiquette
    
    def is_leaf(self):
        return self.value != None