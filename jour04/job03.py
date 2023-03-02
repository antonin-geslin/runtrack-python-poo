class Rectangle():


    def __init__(self, longeur, largeur):
        self.__longeur = longeur
        self.__largeur = largeur

    
    def perimetre(self):
        return (self.__longeur + self.__largeur) * 2

    def surface(self):
        return self.__longeur * self.__largeur

    
    def get_longeur(self):
        return self.__longeur
    
    def get_largeur(self):
        return self.__largeur
    
    def set_longeur(self, longeur):
        self.__longeur = longeur

    def set_largeur(self, largeur):
        self.__largeur = largeur



class Parallepipede(Rectangle):

    def __init__(self, hauteur, largeur, longeur):
        self.__hauteur = hauteur
        Rectangle.__init__(self, longeur, largeur)

    def volume(self):
        return self.__hauteur * self.surface()




rectangle1 = Rectangle(10, 5)
parallepipede1 = Parallepipede(10, 5, 10)

print(rectangle1.surface())
print(rectangle1.perimetre())
print(parallepipede1.perimetre())
print(parallepipede1.surface())
print(parallepipede1.volume())