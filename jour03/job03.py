class Tache():

    def __init__(self, titre, description, statut):
        self.titre = titre
        self.description = description
        self.statut = statut



class ListeTache():

    def __init__(self, taches):
        self.taches = taches

    def ajouterTache(self, Tache):
        self.taches.append(Tache)

    def supprimer(self, Tache):
        self.taches.remove(Tache)

    def marquerCommeFinie(self, Tache):
        Tache.statut = "Terminée"

    def afficherListe(self):
        for tache in self.taches:
            print(tache.titre, tache.description, tache.statut)
        
    def filtrerListe(self, statut):
        for tache in self.taches:
            if tache.statut == statut:
                print(tache.titre, tache.description, tache.statut)
    


tache1 = Tache("Courses", "Description1", "En cours")
tache2 = Tache("Sport", "Description2", "En cours")
tache3 = Tache("Cuisine", "Description3", "Terminée")
tache4 = Tache("Ménage", "Description4", "Terminée")


liste1 = ListeTache([tache1, tache2, tache3])

liste1.ajouterTache(tache4)
liste1.afficherListe()
liste1.supprimer(tache4)
liste1.afficherListe()
liste1.marquerCommeFinie(tache1)
liste1.afficherListe()
liste1.filtrerListe("Terminée")
