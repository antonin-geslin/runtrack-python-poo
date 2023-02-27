class Personnage():

    def __init__(self):
        self.x = 20
        self.y = 20

    def gauche(self):
        self.x += -1

    def droite(self):
        self.x += 1

    def haut(self):
        self.y +=1
    
    def bas(self):
        self.y -=1

    def position(self):
        return(self.x,self.y)


perso1 = Personnage()

perso1.position()
perso1.gauche()
perso1.position()
perso1.droite()
perso1.position()
perso1.haut()
perso1.position()
perso1.bas()
perso1.position()
      