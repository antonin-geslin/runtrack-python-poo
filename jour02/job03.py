class Livre():

    def __init__(self, titre, auteur, nombrePages):
        self.__titre = titre
        self.__auteur = auteur
        self.__nombrePages = nombrePages
        self.__disponible = True


    def set_titre(self, titre):
        self.__titre = titre
    def set_auteur(self, auteur):
        self.__auteur = auteur
    def set_nombrePages(self, nombrePages):
        if nombrePages > 0:
            self.__nombrePages = nombrePages
    def get_titre(self):
        return(self.__titre)
    def get_auteur(self):
        return(self.__auteur)
    def get_nombrePages(self):
        return(self.__nombrePages)
    def get_disponible(self):
        return(self.__disponible)

    def verification(self):
        if self.__disponible == True:
            print("Livre disponible")
            return True
        else:
            print("Livre indisponible")
            return False
    
    def emprunter(self):
        if self.verification():
            self.__disponible = False
            print("Livre emprunté")
        else:
            print("Livre déjà emprunté")
    def rendre(self):
        if self.verification() == False:
            self.__disponible = True
            print("Livre rendu")
        else:
            "Le livre est déjà rendu"


livre1  = Livre("bob", "bob", 5)
livre1.verification()
livre1.emprunter()
livre1.verification()
livre1.rendre()
livre1.verification()
