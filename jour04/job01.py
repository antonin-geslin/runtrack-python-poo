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


class Professeur():

    def __init__(self, matiereEnseignee):
        self.__matiereEnseignee = matiereEnseignee

    def getMatiereEnseignee(self):
        return self.__matiereEnseignee

    def setMatiereEnseignee(self, matiereEnseignee):
        self.__matiereEnseignee = matiereEnseignee

    def enseigner(self):
        print("Le cours va commencer")






personne1 = Personne()
eleve1 = Eleve()


eleve1.afficherAge()

    