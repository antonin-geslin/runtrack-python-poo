class Operation:
    def __init__(self,  nombre1, nombre2):
        self.nombre1 = nombre1
        self.nombre2 = nombre2

    def addition(self):
        print((self.nombre1 + self.nombre2))


ope = Operation(2, 3)

ope.addition()