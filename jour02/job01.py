class Rectangle():
    def __init__(self, longueur, largeur):
        self.__longueur = longueur
        self.__largeur = largeur

    def set_longueur(self, longueur):
        self.__longueur = longueur
    def set_largueur(self, largeur):
        self.__largeur = largeur
    def get_longeur(self):
        return self.__longueur
    def get_largeur(self):
        return self.__largeur



rect1 = Rectangle(10, 5)
print(rect1.get_largeur())
print(rect1.get_longeur())
rect1.set_longueur(11)
rect1.set_largueur(6)
print(rect1.get_largeur())
print(rect1.get_longeur())