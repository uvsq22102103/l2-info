from abc import ABCMeta, abstractmethod

class Point:
    def __init__(self, abscisse:int=0, ordonne:int=0):
        self.__abscisse = abscisse
        self.__ordonne = ordonne
    
    def get_abscisse(self):
        return self.__abscisse
    
    def set_abscisse(self, abscisse):
        self.__abscisse = abscisse
    
    def get_ordonne(self):
        return self.__ordonne
    
    def set_ordonne(self, ordonne):
        self.__ordonne = ordonne

    def cloner(pt):
        return Point(pt.get_abscisse(),pt.get_ordonne())
    
    def afficher(self):
        print(self.get_abscisse(), self.get_ordonne())

class PointColor(Point):
    def __init__(self, color:str, abscisse:int=0, ordonne:int=0):
        super().__init__(abscisse, ordonne)
        self.color = color
    
    def afficher(self):
        Point.afficher(self)
        print(f"couleur : {self.get_color()}")

    def get_color(self):
        return self.color
    
    def set_color(self, color:str):
        self.color = color
    
    def cloner(pt):
        return PointColor(pt.get_color(), pt.get_abscisse(), pt.get_ordonne())

class Forme(metaclass = ABCMeta):
    @abstractmethod
    def __init__(self, points:list[Point|PointColor]):
        self.points = points
    
    @abstractmethod
    def afficher(self):
        for point in self.points:
            point.afficher()
    
    def get_points(self):
        return self.points

    def deplacer(self, x:int, y:int):
        for i in range(len(self.points)):
            if i % 2: # cas y
                self.points[i].set_ordonne(self.points[i].get_ordonne()+y)
            else: # cas x
                self.points[i].set_abscisse(self.points[i].get_abscisse()+x)

class Segment(Forme):
    def __init__(self, pointA:Point, pointB:Point):
        super().__init__([pointA, pointB])
    
    def afficher(self):
        for point in self.get_points():
            point.afficher()

class Triangle(Forme):
    def __init__(self, pointA:Point, pointB:Point, pointC:Point):
        super().__init__([pointA, pointB, pointC])
    
    def afficher(self):
        for point in self.get_points():
            point.afficher()

class Rectangle(Forme):
    def __init__(self, pointA:Point, pointB:Point):
        super().__init__([pointA, pointB])
    
    def afficher(self):
        for point in self.get_points():
            point.afficher()

class Cercle(Forme):
    def __init__(self, point:Point, rayon:int):
        super().__init__([point])
        self.rayon = rayon
    
    def get_rayon(self):
        return self.rayon
    
    def afficher(self):
        for point in self.get_points():
            point.afficher()
        print(f"de rayon {self.get_rayon()}")

ptA = Point(2, 5)
ptB = Point(12, 15)
rec = Rectangle(ptA, ptB)
pt = Point(8, 5)
cer = Cercle(pt, 10)

pt1 = Point(2, 5)
pt2 = Point(3, 7)
pt3 = Point(5, 10)
tri = Triangle(pt1, pt2, pt3)
seg = Segment(pt, pt3)
maliste = [rec, cer, tri, seg]

for elem in maliste:
    elem.afficher()
