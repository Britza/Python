class Punto:
    """Clase que define a un punto en un plano"""

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def getX(self):
        return self.x


class Circulo(Punto):
    def __init__(self, x, y, r):
        Punto.__init__(self,x,y)
        self.r = r




p = Punto(1,3)
c = Circulo(2,3,6)

print(p.getX())
print(c.x)
