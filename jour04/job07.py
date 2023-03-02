import random

class Carte():

    def __init__(self, figure, couleur):
        self.figure = figure
        self.valeur = 0
        self.couleur = couleur

    def calculValeur(self):
        if self.figure == "As":
            self.valeur = (1,11)
        elif self.figure == "Roi" or self.figure == "Dame" or self.figure == "Valet":
            self.valeur = 10
        else:
            self.valeur = int(self.figure)

class Jeu():

    def __init__(self, paquet):
        self.paquet = paquet


    def creerPaquet(self, paquet):
        i = 2
        while i <=10:
            self.paquet.append(Carte(str(i), "Coeur"))
            self.paquet.append(Carte(str(i), "Carreau"))
            self.paquet.append(Carte(str(i), "Trefle"))
            self.paquet.append(Carte(str(i), "Pique"))
            i += 1
        self.paquet.append(Carte("Valet", "Coeur"))
        self.paquet.append(Carte("Valet", "Carreau"))
        self.paquet.append(Carte("Valet", "Trefle"))
        self.paquet.append(Carte("Valet", "Pique"))
        self.paquet.append(Carte("Dame", "Coeur"))
        self.paquet.append(Carte("Dame", "Carreau"))
        self.paquet.append(Carte("Dame", "Trefle"))
        self.paquet.append(Carte("Dame", "Pique"))
        self.paquet.append(Carte("Roi", "Coeur"))
        self.paquet.append(Carte("Roi", "Carreau"))
        self;paquet.append(Carte("Roi", "Trefle"))
        self.paquet.append(Carte("Roi", "Pique"))
        self.paquet.append(Carte("As", "Coeur"))
        self.paquet.append(Carte("As", "Carreau"))
        self.paquet.append(Carte("As", "Trefle"))
        self.paquet.append(Carte("As", "Pique"))

        for i in self.paquet:
            i.calculValeur()


paquet = []
jeu1 = Jeu(paquet)
jeu1.creerPaquet(paquet)
running = True
random1 = 0
random2 = 0

while running:
    print("Bienvenue au BlackJack")
    random1 = random.randint(0, 51)
    random2 = random.randint(0, 51)
    total1 = 0
    total2 = 0
    if paquet[random1].figure == "As":
        paquet[random1].valeur = 11
    elif paquet[random2].figure == "As":
        paquet[random2].valeur = 1
    print("Vous avez pioché : ", paquet[random1].figure, "de ", paquet[random1].couleur, " et ", paquet[random2].figure, "de ", paquet[random2].couleur)
    print("Vous avez donc : ", paquet[random1].valeur + paquet[random2].valeur)
    total1 = paquet[random1].valeur + paquet[random2].valeur
    if total1 == 21:
        print("BlackJack !")
        running = False
        break
    temp = input("Voulez vous tirer ou passer ? y/n")
    if temp == "y" or temp == "Y":
        tirer = True
        while tirer:
            random1 = random.randint(0,51)
            if paquet[random1].figure == "As":
                if total1 + 11 > 21:
                    paquet[random1].valeur = 1
                else:
                    paquet[random1].valeur = 11
            print("Vous avez pioché : ", paquet[random1].figure, "de ", paquet[random1].couleur)
            total1 += paquet[random1].valeur
            print("Vous avez donc : ", total1)
            if total1 > 21:
                print("Busted ! Vous avez perdu")
                tirer = False
                running = False
                break
            elif total1 == 21:
                print("BlackJack !")
                running = False
                tirer = False
                break
            else:
                temp = input("Voulez vous tirer ou passer ? y/n")
                if temp == "n" or temp == "N":
                    random1 = random.randint(0,51)
                    random2 = random.randint(0,51)
                    if paquet[random1].figure == "As":
                        paquet[random1].valeur = 11
                    elif paquet[random2].figure == "As":
                        paquet[random2].valeur = 1
                    print("Le croupier à pioché : ",  paquet[random1].figure, "de ", paquet[random1].couleur, " et ", paquet[random2].figure, "de ", paquet[random2].couleur)
                    print("Il à donc : ", paquet[random1].valeur + paquet[random2].valeur)
                    total2 = paquet[random1].valeur + paquet[random2].valeur
                    if total2 == 21:
                        ("BlackJack ! Vous avez perdu ")
                        tirer = False
                        running = False
                        break
                    croupier = True
                    while croupier:
                        if total2 < 17:
                            random1 = random.randint(0,51)
                            if paquet[random1].figure == "As":
                                if total2 + 11 > 21:
                                    paquet[random1].valeur = 1
                                else:
                                    paquet[random1].valeur = 11
                            print("Le croupier à pioché : ",  paquet[random1].figure, "de ", paquet[random1].couleur)
                            total2 += paquet[random1].valeur
                            print("Il à donc : ", total2)
                            if total2 > 21:
                                print("Le croupier Bust vous avez gagné !")
                                croupier = False
                                running = False
                                break
                            elif total2 == 21:
                                print("Le croupier fait BlackJack")
                                croupier = False
                                running = False
                                break
                        else:
                            croupier = False

                    
                    if total1 > total2:
                        print("Vous avez gagné")
                        running = False
                        break
                    elif total1 < total2:
                        print("Le croupier gagne")
                        running = False
                        break
                    elif total1 == total2:
                        ("Vous regagnez votre mise")
                        running = False
                        break
                        
    elif (temp == "n" or temp == "N") or croupier == True :
        random1 = random.randint(0,51)
        random2 = random.randint(0,51)
    if paquet[random1].figure == "As":
        paquet[random1].valeur = 11
    elif paquet[random2].figure == "As":
        paquet[random2].valeur = 1
        print("Le croupier à pioché : ",  paquet[random1].figure, "de ", paquet[random1].couleur, " et ", paquet[random2].figure, "de ", paquet[random2].couleur)
        print("Il à donc : ", paquet[random1].valeur + paquet[random2].valeur)
        total2 = paquet[random1].valeur + paquet[random2].valeur
        if total2 == 21:
            ("BlackJack ! Vous avez perdu ")
            running = False
            break
        tirer = True
        while tirer:
            if total2 < 17:
                random1 = random.randint(0,51)
                if paquet[random1].figure == "As":
                    if total2 + 11 > 21:
                        paquet[random1].valeur = 1
                    else:
                        paquet[random1].valeur = 11
                print("Le croupier à pioché : ",  paquet[random1].figure, "de ", paquet[random1].couleur)
                total2 += paquet[random1].valeur
                print("Il à donc : ", total2)
                if total2 > 21:
                    print("Le croupier Bust vous avez gagné !")
                    running = False
                    break
                elif total2 == 21:
                    print("Le croupier fait BlackJack")
                    running = False
                    break
            else:
                tirer = False

        
        if total1 > total2:
            print("Vous avez gagné")
            running = False
        elif total1 < total2:
            print("Le croupier gagne")
            running = False
        elif total1 == total2:
            ("Vous regagnez votre mise")
            running = False
            




    