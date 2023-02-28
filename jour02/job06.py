class Commande():

    def __init__(self, numeroCommande, listePlatCommandes, statutCommande):
        self.__numeroCommande = numeroCommande
        self.__listePlatCommandes = listePlatCommandes
        self.__statutCommande = statutCommande


    def get_numeroCommande(self):
        return(self.__numeroCommande)

    def get_listePlatCommandes(self):
        return(self.__listePlatCommandes)
    
    def get_statutCommande(self):
        return(self.__statutCommande)

    def set_numeroCommande(self, numeroCommande):
        self.__numeroCommande = numeroCommande
    
    def set_statutCommande(self, statutCommande):
        self.__statutCommande = statutCommande

    def ajouterPlat(self, plat, prix):
        self.__listePlatCommandes[plat] = prix

    def annulerCommande(self):
        self.set_statutCommande("Annulée")

    def __totalCommande(self):
        count = 0
        for i in self.__listePlatCommandes:
            count += self.__listePlatCommandes[i]
        return(count)
    
    def TVA(self, TVA):
        temp = self.__totalCommande() * TVA
        prixTTC = temp + self.__totalCommande()
        return(prixTTC)

    def recuCommande(self, TVA):
        print("Commande", self.get_listePlatCommandes())
        print("Prix ", self.TVA(TVA))
        print("Statut ", self.get_statutCommande())



listePlat = {"Burger" : 12 , "Pizza" : 12, "Pates" : 12  }
commande1 = Commande(12, listePlat, "en cours")
commande1.recuCommande(0.2)
commande1.ajouterPlat("Salade", 12)
commande1.recuCommande(0.2)
commande1.annulerCommande()
commande1.recuCommande(0.2)

