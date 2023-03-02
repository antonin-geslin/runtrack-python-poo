class Forme():

    def aire(self):
        return 0


class Cercle(Forme):

    def __init__(self, radius):
        self.__radius = radius


    def aire(self):
        return 3.14 * self.__radius * self.__radius


class Rectangle(Forme):

    def __init__(self, longeur, largeur):
        self.__longeur = longeur
        self.__largeur = largeur

    def aire(self):
        return self.__longeur * self.__largeur



rectangle1 = Rectangle(10, 5)
cercle1 = Cercle(10)

print(rectangle1.aire())
print(cercle1.aire())