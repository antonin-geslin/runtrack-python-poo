class Voiture():

    def __init__(self, marque, modele, annee, kilometrage):
        self.__marque = marque
        self.__modele = modele
        self.__annee = annee
        self.__kilometrage = kilometrage 
        self.__enMarche = False
        self.__reservoir = 50


    def get_marque(self):
        return(self.__marque)
    def get_annee(self):
        return(self.__annee)
    def get_modele(self):
        return(self.__modele)
    def get_kilometrage(self):
        return(self.__kilometrage)
    def get_enMarche(self):
        return(self.__enMarche)
    def set_reservoir(self, reservoir):
        self.__reservoir = reservoir
    def set_marque(self, marque):
        self.__marque = marque
    def set_annee(self, annee):
        self.__annee = annee
    def set_modele(self, modele):
        self.__modele = modele
    def set_kilometrage(self, kilometrage):
        self.__kilometrage = kilometrage
    def set_enMarche(self, enMarche):
        self.__enMarche = enMarche

    def demarrer(self):
        if self.get_enMarche() == False:
            if self.__verifierPlein() > 5:
                self.set_enMarche(True)
            else:
                print("Pas assez d'essence")
        else:
            print("La voiture à déjà démarrée")

    def arreter(self):
        if self.get_enMarche():
            self.set_enMarche(False)
        else:
            print("La voiture à déjà éteinte")

    def __verifierPlein(self):
        return(self.__reservoir)




voiture1 = Voiture("Renault", "Clio", 2002, 100000)

print(voiture1.get_enMarche())
voiture1.demarrer()
print(voiture1.get_enMarche())
voiture1.arreter()
print(voiture1.get_enMarche())
voiture1.set_reservoir(4)
voiture1.demarrer()
print(voiture1.get_enMarche())