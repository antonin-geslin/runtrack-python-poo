class Produit():

    def __init__(self, nom, prixHT, TVA):
        self.nom = nom
        self.prixHT = prixHT
        self.TVA = TVA

    def calculerPrixTTC(self):
        prixTTC = self.prixHT * self.TVA
        prixTTC += self.prixHT
        return(prixTTC)

    def afficher(self):
        return(self.nom, self.prixHT, self.TVA, self.calculerPrixTTC())
    
    def nom(self):
        return(self.nom)
    
    def prix(self):
        return(self.prix)

    def tva(self):
        return(self.tva)

    def ttc(self):
        return(self.calculerPrixTTC())

    def modifNom(self, nom):
        self.nom = nom

    def modifPrix(self, prix):
        self.prix = prix

produit1 = Produit("Telephone", 300, 0.2)
produit2 = Produit("Saucisse", 2, 0.2)

print(produit1.afficher())
print(produit2.afficher())

produit1.modifNom("Tablette")
produit1.modifPrix(400)
produit2.modifNom("Merguez")
produit2.modifPrix(1.50)

print(produit1.afficher())
print(produit2.afficher())