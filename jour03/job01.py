class Ville():

    def __init__(self, nom, nombreHabitants):
        self.nom = nom
        self.nombreHabitants = nombreHabitants

    def get_nom(self):
        return self.nom
    def get_nombreHabitants(self):
        return self.nombreHabitants
    


class Personne():

    def __init__(self, nom, age, ville):
        self.nom = nom
        self.age = age
        self.ville = ville


    def ajouterPopulation(self):
        self.ville.nombreHabitants += 1
    



ville1 = Ville("Paris", 1000000)
ville2 = Ville("Marseille", 800000)
print(ville1.get_nombreHabitants())
print(ville2.get_nombreHabitants())

personne1 = Personne("John", 45, ville1)
personne2 = Personne("Myrtille", 4, ville1)
personne3 = Personne("Chloé", 18, ville2)

personne1.ajouterPopulation()
personne2.ajouterPopulation()
personne3.ajouterPopulation()

print(ville1.get_nombreHabitants())
print(ville2.get_nombreHabitants())