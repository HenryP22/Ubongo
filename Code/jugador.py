class player(object):
    def __init__(self):
        self.ruta = [None] * 0
        self.colores = [None]*0
        self.ultimo = 0

    def tomarGema(self, a):
        self.ruta.append(a)
        self.ruta.append(a + 6)
        self.ultimo = a + 6

    def mostrar(self):
        print(self.ruta)
        print(self.ultimo)