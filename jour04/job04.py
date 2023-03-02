

class Forme():

    def aire(self):
        return 0



class Rectangle(Forme):

    def __init__(self, longeur, largeur):
        self.__longeur = longeur
        self.__largeur = largeur

    def aire(self):
        return self.__longeur * self.__largeur




rectangle1 = Rectangle(10, 5)

print(rectangle1.aire())