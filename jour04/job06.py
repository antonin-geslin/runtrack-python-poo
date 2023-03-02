class Vehicule():

    def __init__(self, marque, modele, annee, prix):
        self.marque = marque
        self.modele = modele
        self.annee = annee
        self.prix = prix


    def informationsVehicule(self):
        print("Marque: " + self.marque)
        print("Modèle: " + self.modele)
        print("Année: " + str(self.annee))
        print("Prix: " + str(self.prix))



class Voiture(Vehicule):

    def __init__(self, marque, modele,  annee, prix):
        self.nombreDePortes = 4
        Vehicule.__init__(self, marque, modele, annee, prix)


    def informationsVehicule(self):
        Vehicule.informationsVehicule(self)
        print("Nombre de portes: " + str(self.nombreDePortes))

class Moto(Vehicule):

    def __init__(self, marque, modele,  annee, prix):
        self.roues = 2
        Vehicule.__init__(self, marque, modele, annee, prix)


    def informationsVehicule(self):
        Vehicule.informationsVehicule(self)
        print("Nombre de roues: " + str(self.roues))

voiture1 = Voiture("Mercedes", "Classe a", 2020, 50000) 
moto1 = Moto("Yamaha", "R1", 2019, 30000)
voiture1.informationsVehicule()
moto1.informationsVehicule()