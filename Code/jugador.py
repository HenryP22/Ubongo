class player(object):
    def __init__(self):
        self.ruta = [None] * 0
        self.colores = [None] * 0
        self.ultimo = 0
        self.amarillos = 0
        self.azul = 0
        self.marron = 0
        self.morada = 0
        self.roja = 0
        self.verde = 0
        self.prioridad = 0
        self.prioridadColor = 0

    def tomarGema(self, fila, od):
        self.ruta.append(fila)
        self.ruta.append(fila + 6)
        self.colores.append(od.colores[fila])
        self.contarGema(fila,od)
        self.colores.append(od.colores[fila + 6])
        self.contarGema(fila + 6, od)
        self.fijarprioridad()

    def contarGema(self, fila, od):
        if od.colores[fila] == 1:
            self.amarillos = self.amarillos + 1
        elif od.colores[fila] == 2:
            self.azul = self.azul + 1
        elif od.colores[fila] == 3:
            self.marron = self.marron + 1
        elif od.colores[fila] == 4:
            self.morada = self.morada + 1
        elif od.colores[fila] == 5:
            self.roja = self.roja + 1
        elif od.colores[fila] == 6:
            self.verde = self.verde + 1

    def conteo(self):
        return self.prioridad



    def fijarprioridad(self):
        if self.prioridad < self.amarillos:
            self.prioridad = self.amarillos
            self.prioridadColor = 1
        elif self.prioridad < self.azul:
            self.prioridad = self.azul
            self.prioridadColor = 2
        elif self.prioridad < self.marron:
            self.prioridad = self.marron
            self.prioridadColor = 3
        elif self.prioridad < self.morada:
            self.prioridad = self.morada
            self.prioridadColor = 4
        elif self.prioridad < self.roja:
            self.prioridad = self.roja
            self.prioridadColor = 5
        elif self.prioridad < self.verde:
            self.prioridad = self.verde
            self.prioridadColor = 6

    def mostrar(self):
        print(self.ruta)
        print(self.prioridad)

