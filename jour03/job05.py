class Personnage():

    def __init__(self, nom, vie):
        self.nom = nom
        self.vie = vie

    def attaquer(self, Personnage):
        Personnage.vie -= 10



class Jeu():


    def choisirNiveau(self):
        niveau = input("Choisissez un niveau de difficulté (1, 2 ou 3): ")
        return(int(niveau))


    def lancerJeu(self, niveau):
        if niveau == 1:
            self.joueur1 = Personnage("John", 100)
            self.joueur2 = Personnage("Myrtille", 100)
        elif niveau == 2:
            self.joueur1 = Personnage("John", 150)
            self.joueur2 = Personnage("Myrtille", 150)
        elif niveau == 3:
            self.joueur1 = Personnage("John", 200)
            self.joueur2 = Personnage("Myrtille", 200)
        else:
            print("Niveau de difficulté incorrect")
            return

        while self.joueur1.vie > 0 and self.joueur2.vie > 0:
            self.joueur1.attaquer(self.joueur2)
            self.joueur2.attaquer(self.joueur1)
            print("Joueur 1: ", self.joueur1.vie)
            print("Joueur 2: ", self.joueur2.vie)

        if self.joueur1.vie > 0:
            print("Le joueur 1 a gagné")
        else:
            print("Le joueur 2 a gagné")


jeu = Jeu()
jeu.lancerJeu(jeu.choisirNiveau())