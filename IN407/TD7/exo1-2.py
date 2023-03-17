#######################
######## CLASS ########

class Point():
    """Exercice 1"""
    def __init__(self, abscisse:int=0, ordonne:int=0):
        self.__abscisse = abscisse
        self.__ordonne = ordonne
    
    def get_coords(self):
        return (self.__abscisse, self.__ordonne)
    
    def cloner(pt):
        x, y = pt.get_coords()
        return Point(x,y)
    
    def afficher(self):
        print(self.__abscisse, self.__ordonne)


class Segment():
    """Exercice 2"""
    def __init__(self, ptA:Point, ptB:Point):
        self.ptA = ptA
        self.ptB = ptB
    
    def est_vertical(self):
        return self.ptA.get_coords()[0] == self.ptB.get_coords()[0]
    
    def est_horizontal(self):
        return self.ptA.get_coords()[1] == self.ptB.get_coords()[1]
    
    def est_diagonal(self):
        return not self.est_horizontal() and not self.est_diagonal()
    
    def longeur(self):
        """sqrt((xB-xA)**2 + (yB-yA)**2)"""
        xA, yA = self.ptA.get_coords()
        xB, yB = self.ptB.get_coords()
        return ((xB-xA)**2 + (yB-yA)**2)**(1/2)

########################
######### MAIN #########

pt1 = Point(1,3)
pt2 = Point(9,6)
pt1.afficher()
pt2.afficher()
seg1 = Segment(pt1, pt2)
print(seg1.longeur())

pt3 = Point.cloner(pt1)
pt3.afficher()
