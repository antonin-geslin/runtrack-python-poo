class Point():

    def __init__(self):
        self.x = 20
        self.y = 20

    def afficherLesPoints(self):
        print("x : ", self.x, "y : ", self.y)

    def afficherX(self):
        print("x : ", self.x)

    def afficherY(self):
        print("y : ", self.y)

    def changerX(self, x):
        self.x = x

    def changerY(self, y):
        self.y = y

point1 = Point()
point1.afficherLesPoints()
point1.afficherX()
point1.afficherY()
point1.changerX(30)
point1.changerY(30)
point1.afficherLesPoints()