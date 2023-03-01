class Joueur():

    def __init__(self, nom, numero, position, nombresBut, nombrePasses,  cartonsJ, cartonsR):
        self.nom = nom
        self.numero = numero
        self.position = position
        self.nombresBut = nombresBut
        self.cartonsJ = cartonsJ
        self.cartonsR = cartonsR
        self.nombrePasses = nombrePasses
    
    def marquerUnBut(self):
        self.nombresBut += 1
        print("Le joueur ", self.nom, "a marqué un but")

    def effectuerUnePasseDecisive(self):
        self.nombrePasses += 1
        print("Le joueur ", self.nom, "a effectué une passe décisive")

    def recevoirUnCartonJaune(self):
        self.cartonsJ += 1
        print("Le joueur ", self.nom, "a reçu un carton jaune")

    def recevoirUnCartonRouge(self):
        self.cartonsR += 1
        print("Le joueur ", self.nom, "a reçu un carton rouge")

    def afficherStatistiques(self):
        print("Le joueur ", self.nom, "a marqué ", self.nombresBut, "but(s)")
        print("Le joueur ", self.nom, "a effectué ", self.nombrePasses, "passe(s) décisive(s)")
        print("Le joueur ", self.nom, "a reçu ", self.cartonsJ, "carton(s) jaune(s)")
        print("Le joueur ", self.nom, "a reçu ", self.cartonsR, "carton(s) rouge(s)")


class Equipe():

    def __init__(self, nom):
        self.nom = nom
        self.listeJoueurs = []


    def ajouterJoueur(self, joueur):
        self.listeJoueurs.append(joueur)

    def afficherStatistiquesJoueur(self):
        for joueur in self.listeJoueurs:
            joueur.afficherStatistiques()


    def mettreAJourStatistiquesJoueur(self, Joueur, but, cartonsR, cartonsJ, passes):
        if but == 1:
            Joueur.marquerUnBut()
        if cartonsR == 1:
            Joueur.recevoirUnCartonRouge()
        if cartonsJ == 1:
            Joueur.recevoirUnCartonJaune()
        if passes == 1:
            Joueur.effectuerUnePasseDecisive()

joueur1 = Joueur("John", 10, "Attaquant", 0, 0, 0, 0)
joueur2 = Joueur("Myrtille", 11, "Attaquant", 0, 0, 0, 0)
joueur3 = Joueur("Chloé", 12, "Defenseur", 0, 0, 0, 0)
joueur4 = Joueur("Jean", 13, "Defenseur", 0, 0, 0, 0)
joueur5 = Joueur("Paul", 14, "Milieu", 0, 0, 0, 0)


joueur6 = Joueur("Bob", 10, "Attaquant", 0, 0, 0, 0)
joueur7 = Joueur("Marie", 11, "Attaquant", 0, 0, 0, 0)
joueur8 = Joueur("Pierre", 12, "Defenseur", 0, 0, 0, 0)
joueur9 = Joueur("Jacques", 13, "Defenseur", 0, 0, 0, 0)
joueur10 = Joueur("Jeanne", 14, "Milieu", 0, 0, 0, 0)


equipe1 = Equipe("Marseille")
equipe2 = Equipe("Paris")


equipe1.ajouterJoueur(joueur1)
equipe1.ajouterJoueur(joueur2)
equipe1.ajouterJoueur(joueur3)
equipe1.ajouterJoueur(joueur4)
equipe1.ajouterJoueur(joueur5)

equipe2.ajouterJoueur(joueur6)
equipe2.ajouterJoueur(joueur7)
equipe2.ajouterJoueur(joueur8)
equipe2.ajouterJoueur(joueur9)
equipe2.ajouterJoueur(joueur10)

equipe1.afficherStatistiquesJoueur()
equipe2.afficherStatistiquesJoueur()



equipe1.mettreAJourStatistiquesJoueur(joueur1, 1, 0, 0, 0)
equipe1.mettreAJourStatistiquesJoueur(joueur2, 0, 0, 0, 1)
equipe2.mettreAJourStatistiquesJoueur(joueur3, 0, 0, 1, 0)
equipe2.mettreAJourStatistiquesJoueur(joueur4, 1, 0, 0, 0)
equipe2.mettreAJourStatistiquesJoueur(joueur5, 0, 0, 0, 1)
equipe1.afficherStatistiquesJoueur()