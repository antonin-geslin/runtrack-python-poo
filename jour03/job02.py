class CompteBancaire():
    
    def __init__(self, numeroCompte, nom, prenom, solde,  decouvert):
        self.numeroCompte = numeroCompte
        self.nom = nom
        self.prenom = prenom
        self.solde = solde
        self.decouvert = decouvert

    def afficherSolde(self):
        print("Le solde du compte est de ", self.solde, "€")
    
    def versement(self, montant):
        self.solde += montant
        print("Le solde du compte est de ", self.solde, "€")

    def retrait(self, montant):
        if montant < self.solde:
            self.solde -= montant
            print("Le solde du compte est de ", self.solde, "€")
        elif self.decouvert:
            self.solde -= montant
            print("Le solde du compte est de ", self.solde, "€")
        else:
            print("Le solde du compte est insuffisant")

    def afficher(self):
        print("Le prénom du titulaire est ", self.prenom)
        print("Le nom du titulaire est ", self.nom)
        print("Le numéro de compte est ", self.numeroCompte)
        print("Le solde du compte est de ", self.solde, "€")


    def virement(self, compte, montant):
        if montant < self.solde:
            self.solde -= montant
            compte.solde += montant
            print("Le solde du compte est de ", self.solde, "€")
        elif self.decouvert:
            self.solde -= montant
            compte.solde += montant
            print("Le solde du compte est de ", self.solde, "€")
        else:
            print("Le solde du compte est insuffisant")

    def agios(self):
        if self.solde < 0:
            self.solde -= 20
            print("Le solde du compte est de ", self.solde, "€")
        else:
            print("Le solde du compte est positif")




compte1 = CompteBancaire(123456789, "Dupont", "Jean", 10000, False)
compte2 = CompteBancaire(987654321, "Durand", "Marie", -1000, True)

compte1.afficher()
compte1.versement(500)
compte1.afficher()
compte1.retrait(2000)
compte1.retrait(1000)
compte1.agios()
compte1.afficher()

compte1.virement(compte2,1000)
compte2.afficher()