class Personne():

    def __init__(self, nom, prenom):
        self.prenom = prenom
        self.nom = nom


    def sePresenter(self):
        print("Je suis ", self.prenom,self.nom)




personne1 = Personne("Jhon", "Doe")
personne2 = Personne("Jean", "Dupond")

personne1.sePresenter()
personne2.sePresenter()