class Personne():

    def __init__(self):
        self.age = 14


    def afficherAge(self):
        print(self.age)

    def bonjour(self):
        print("Hello")


    def modifierAge(self, age):
        self.age = age



    
class Eleve(Personne):
    
    def __init__(self):
        Personne.__init__(self)

    def allerEnCour(self):
        print("Je vais en cours")


class Professeur(Personne):

    def __init__(self, matiereEnseignee):
        self.__matiereEnseignee = matiereEnseignee
        Personne.__init__(self)

    def getMatiereEnseignee(self):
        return self.__matiereEnseignee

    def setMatiereEnseignee(self, matiereEnseignee):
        self.__matiereEnseignee = matiereEnseignee

    def enseigner(self):
        print("Le cours va commencer")




eleve1 = Eleve()

eleve1.bonjour()
eleve1.allerEnCour()
eleve1.modifierAge(15)
eleve1.afficherAge()

professeur1 = Professeur("Maths")
professeur1.modifierAge(40)
professeur1.afficherAge()
professeur1.bonjour()
professeur1.enseigner()