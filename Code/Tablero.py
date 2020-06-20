from time import sleep

import pygame, sys
import graphviz
import random
# Setup pygame/window ---------------------------------------- #
mainClock = pygame.time.Clock()
from pygame.locals import *

pygame.init()
pygame.display.set_caption('Ubongo')
screen = pygame.display.set_mode((1280, 720), 0, 32)
font = pygame.font.SysFont(None, 20)

tableroImg = pygame.image.load('tablero ubongo.png')

amarillaImg = pygame.image.load('gema amarilla.png')
azulImg = pygame.image.load('gema azul.png')
marronImg = pygame.image.load('gema marron.png')
moradaImg = pygame.image.load('gema morada.png')
rojaImg = pygame.image.load('gema roja.png')
verdeImg = pygame.image.load('gema verde.png')
imagen1 = pygame.image.load("cara1.png")
imagen2 = pygame.image.load("cara2.png")
imagen3 = pygame.image.load("cara3.png")
imagen4 = pygame.image.load("cara4.png")
imagen5 = pygame.image.load("cara5.png")
imagen6 = pygame.image.load("cara6.png")
def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)
click = False

#-------------------------------------------------------
class Grafo(object):
    def __init__(self, n):
        self.G = graphviz.Digraph()
        self.n = n
        self.visitados = [False] * n
        self.colores = [None] * n
        self.ruta = [None] * n

    def crear(self):
        gema_list = [1, 2, 3, 4, 5, 6]
        for i in range(self.n):
            m = random.choice(gema_list)
            self.G.node(str(i), str(m))
            self.colores[i] = m

    def conectarTodo(self):
        h = 5
        c = 1
        for i in range(self.n - 6):
            for j in range(6):
                j = (i + h) + c
                self.G.edge(str(i), str(j))
                c = c + 1
                if c == 7:
                    c = 1
            h = h - 1
            if h == -1:
                h = 5

    def tomarGema(self, a, ultimo):
        if self.visitados[a] == False:
            self.G.edge(str(a), str(a + 6))
            self.G.edge(str(ultimo), str(a))
            self.visitados[a] = True
            self.visitados[a + 6] = True
        else:
            return

    def mostrar(self):
        self.G.graph_attr['rankdir'] = 'LR'
        return graphviz.Source(self.G)



od = Grafo(72)
od.crear()
#-------------------------------------------------------

def Base():
    screen.blit(tableroImg, (0, 0))
def dado(n):
    if n == 1:
        screen.blit(imagen1, (140, 560))
    elif n == 2:
        screen.blit(imagen2, (140, 560))
    elif n == 3:
        screen.blit(imagen3, (140, 560))
    elif n == 4:
        screen.blit(imagen4, (140, 560))
    elif n == 5:
        screen.blit(imagen5, (140, 560))
    elif n == 6:
        screen.blit(imagen6, (140, 560))
def tabla():
    x = 423
    y = 98
    a = 0
    for i in range(12):
        y = 98
        for j in range(6):
            if od.colores[a] == 1 and od.visitados[a] == False:
                screen.blit(amarillaImg, (x, y))
            elif od.colores[a] == 2 and od.visitados[a] == False:
                screen.blit(azulImg, (x, y))
            elif od.colores[a] == 3 and od.visitados[a] == False:
                screen.blit(marronImg, (x, y))
            elif od.colores[a] == 4 and od.visitados[a] == False:
                screen.blit(moradaImg, (x, y))
            elif od.colores[a] == 5 and od.visitados[a] == False:
                screen.blit(rojaImg, (x, y))
            elif od.colores[a] == 6 and od.visitados[a] == False:
                screen.blit(verdeImg, (x, y))
            a = a + 1
            y = y + 51
        x = x + 63

def GemasJ1():
    x = 120
    y= 434
    n = len(j1.ruta)
    for i in range(n):
        if j1.colores[i] == 1:
            screen.blit(amarillaImg, (x, y))
        elif j1.colores[i] == 2:
            screen.blit(azulImg, (x, y))
        elif j1.colores[i] == 3:
            screen.blit(marronImg, (x, y))
        elif j1.colores[i] == 4:
            screen.blit(moradaImg, (x, y))
        elif j1.colores[i] == 5:
            screen.blit(rojaImg, (x, y))
        elif j1.colores[i] == 6:
            screen.blit(verdeImg, (x, y))
        x = x + 35
        if(x>360):
            x=120
            y=y+32

def GemasJ2():
    x = 380
    y= 434
    n = len(j2.ruta)
    for i in range(n):
        if j2.colores[i] == 1:
            screen.blit(amarillaImg, (x, y))
        elif j2.colores[i] == 2:
            screen.blit(azulImg, (x, y))
        elif j2.colores[i] == 3:
            screen.blit(marronImg, (x, y))
        elif j2.colores[i] == 4:
            screen.blit(moradaImg, (x, y))
        elif j2.colores[i] == 5:
            screen.blit(rojaImg, (x, y))
        elif j2.colores[i] == 6:
            screen.blit(verdeImg, (x, y))
        x = x + 35
        if(x>620):
            x=380
            y=y+32

def GemasJ3():
    x = 650
    y= 434
    n = len(j3.ruta)
    for i in range(n):
        if j3.colores[i] == 1:
            screen.blit(amarillaImg, (x, y))
        elif j3.colores[i] == 2:
            screen.blit(azulImg, (x, y))
        elif j3.colores[i] == 3:
            screen.blit(marronImg, (x, y))
        elif j3.colores[i] == 4:
            screen.blit(moradaImg, (x, y))
        elif j3.colores[i] == 5:
            screen.blit(rojaImg, (x, y))
        elif j3.colores[i] == 6:
            screen.blit(verdeImg, (x, y))
        x = x + 35
        if(x>890):
            x=650
            y=y+32

def GemasJ4():
    x = 920
    y= 434
    n = len(j4.ruta)
    for i in range(n):
        if j4.colores[i] == 1:
            screen.blit(amarillaImg, (x, y))
        elif j4.colores[i] == 2:
            screen.blit(azulImg, (x, y))
        elif j4.colores[i] == 3:
            screen.blit(marronImg, (x, y))
        elif j4.colores[i] == 4:
            screen.blit(moradaImg, (x, y))
        elif j4.colores[i] == 5:
            screen.blit(rojaImg, (x, y))
        elif j4.colores[i] == 6:
            screen.blit(verdeImg, (x, y))
        x = x + 35
        if(x>1160):
            x=920
            y=y+32



#-------------------------------------------------------
class jugador(object):
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

j1 = jugador()
j2 = jugador()
j3 = jugador()
j4 = jugador()

#-------------------------------------------------------
class TableroUbongo(object):
    def __init__(self):
        self.jugador = 1
        self.fila1=0
        self.fila2=1
        self.fila3=2
        self.fila4=3
        self.fila5=4
        self.fila6=5
        self.tiempo = 0



    def tablero(self):
        running = True
        n = 0
        enum = 0
        while running:
            screen.fill((0, 0, 0))
            draw_text('tablero', font, (255, 255, 255), screen, 20, 20)

            mx, my = pygame.mouse.get_pos()

            button_fila1 = pygame.Rect(300, 98, 30, 30)
            button_fila2 = pygame.Rect(300, 149, 30, 30)
            button_fila3 = pygame.Rect(300, 200, 30, 30)
            button_fila4 = pygame.Rect(300, 251, 30, 30)
            button_fila5 = pygame.Rect(300, 302, 30, 30)
            button_fila6 = pygame.Rect(300, 353, 30, 30)
            button_iniciar = pygame.Rect(1095, 595, 50, 50)
            t=jugador()


            if button_fila1.collidepoint((mx, my)):
                if click:
                    od.visitados[self.fila1] = True
                    od.visitados[self.fila1 + 6] = True
                    if self.jugador == 1:
                        t = j1
                    elif self.jugador == 2:
                        t = j2
                    elif self.jugador == 3:
                        t = j3
                    elif self.jugador == 4:
                        t = j4
                    t.ruta.append(self.fila1)
                    t.ruta.append(self.fila1 + 6)
                    t.colores.append(od.colores[self.fila1])
                    t.colores.append(od.colores[self.fila1 + 6])
                    self.fila1 = self.fila1 + 12
                    if self.jugador==1:
                        t=j1
                    elif self.jugador==2:
                        t=j2
                    elif self.jugador==3:
                        t=j3
                    elif self.jugador==4:
                        t=j4
                    pygame.display.update()

            if button_fila2.collidepoint((mx, my)):
                if click:
                    od.visitados[self.fila2] = True
                    od.visitados[self.fila2 + 6] = True
                    if self.jugador == 1:
                        t = j1
                    elif self.jugador == 2:
                        t = j2
                    elif self.jugador == 3:
                        t = j3
                    elif self.jugador == 4:
                        t = j4
                    t.ruta.append(self.fila2)
                    t.ruta.append(self.fila2 + 6)
                    t.colores.append(od.colores[self.fila2])
                    t.colores.append(od.colores[self.fila2 + 6])
                    self.fila2 = self.fila2 + 12
                    if self.jugador == 1:
                        t = j1
                    elif self.jugador == 2:
                        t = j2
                    elif self.jugador == 3:
                        t = j3
                    elif self.jugador == 4:
                        t = j4
                    pygame.display.update()

            if button_fila3.collidepoint((mx, my)):
                if click:
                    od.visitados[self.fila3] = True
                    od.visitados[self.fila3 + 6] = True
                    if self.jugador == 1:
                        t = j1
                    elif self.jugador == 2:
                        t = j2
                    elif self.jugador == 3:
                        t = j3
                    elif self.jugador == 4:
                        t = j4
                    t.ruta.append(self.fila3)
                    t.ruta.append(self.fila3 + 6)
                    t.colores.append(od.colores[self.fila3])
                    t.colores.append(od.colores[self.fila3 + 6])
                    self.fila3 = self.fila3 + 12
                    if self.jugador == 1:
                        t = j1
                    elif self.jugador == 2:
                        t = j2
                    elif self.jugador == 3:
                        t = j3
                    elif self.jugador == 4:
                        t = j4
                    pygame.display.update()

            if button_fila4.collidepoint((mx, my)):
                if click:
                    od.visitados[self.fila4] = True
                    od.visitados[self.fila4 + 6] = True
                    if self.jugador == 1:
                        t = j1
                    elif self.jugador == 2:
                        t = j2
                    elif self.jugador == 3:
                        t = j3
                    elif self.jugador == 4:
                        t = j4
                    t.ruta.append(self.fila4)
                    t.ruta.append(self.fila4 + 6)
                    t.colores.append(od.colores[self.fila4])
                    t.colores.append(od.colores[self.fila4 + 6])
                    self.fila4 = self.fila4 + 12
                    if self.jugador == 1:
                        t = j1
                    elif self.jugador == 2:
                        t = j2
                    elif self.jugador == 3:
                        t = j3
                    elif self.jugador == 4:
                        t = j4
                    pygame.display.update()

            if button_fila5.collidepoint((mx, my)):
                if click:
                    od.visitados[self.fila5] = True
                    od.visitados[self.fila5 + 6] = True
                    if self.jugador == 1:
                        t = j1
                    elif self.jugador == 2:
                        t = j2
                    elif self.jugador == 3:
                        t = j3
                    elif self.jugador == 4:
                        t = j4
                    t.ruta.append(self.fila5)
                    t.ruta.append(self.fila5 + 6)
                    t.colores.append(od.colores[self.fila5])
                    t.colores.append(od.colores[self.fila5 + 6])
                    self.fila5 = self.fila5 + 12
                    if self.jugador == 1:
                        t = j1
                    elif self.jugador == 2:
                        t = j2
                    elif self.jugador == 3:
                        t = j3
                    elif self.jugador == 4:
                        t = j4
                    pygame.display.update()

            if button_fila6.collidepoint((mx, my)):
                if click:
                    od.visitados[self.fila6] = True
                    od.visitados[self.fila6 + 6] = True
                    if self.jugador == 1:
                        t = j1
                    elif self.jugador == 2:
                        t = j2
                    elif self.jugador == 3:
                        t = j3
                    elif self.jugador == 4:
                        t = j4
                    t.ruta.append(self.fila6)
                    t.ruta.append(self.fila6 + 6)
                    t.colores.append(od.colores[self.fila6])
                    t.colores.append(od.colores[self.fila6 + 6])
                    self.fila6 = self.fila6 + 12
                    if self.jugador == 1:
                        t = j1
                    elif self.jugador == 2:
                        t = j2
                    elif self.jugador == 3:
                        t = j3
                    elif self.jugador == 4:
                        t = j4
                    pygame.display.update()

            if (1095 < mx < 1145 and 600 < my < 650):
                enum = random.randint(1, 6)
                n = random.randint(1, 6)
            if (140 < mx < 240 and 560 < my < 660):
                if (enum == 1):
                    import Puzzle1
                    Puzzle1.main()
                if (enum == 2):
                    import Puzzle2
                    Puzzle2.main()
                if (enum == 3):
                    import Puzzle3
                    Puzzle3.main()
                if (enum == 4):
                    import Puzzle4
                    Puzzle4.main()
                if (enum == 5):
                    import Puzzle5
                    Puzzle5.main()
                if (enum == 6):
                    import Puzzle6
                    Puzzle6.main()

            click = False

            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        running = False
                    if event.key == K_a:
                        self.jugador=1
                    if event.key == K_b:
                        self.jugador=2
                    if event.key == K_c:
                        self.jugador=3
                    if event.key == K_d:
                        self.jugador=4
                if event.type == MOUSEBUTTONDOWN:
                    if event.button == 1:
                        click = True

            Base()
            tabla()
            GemasJ1()
            GemasJ2()
            GemasJ3()
            GemasJ4()
            if button_iniciar.collidepoint((mx,my)):
                if click:
                    pass
            pygame.draw.rect(screen, (255, 0, 0), button_fila1)
            pygame.draw.rect(screen, (255, 0, 0), button_fila2)
            pygame.draw.rect(screen, (255, 0, 0), button_fila3)
            pygame.draw.rect(screen, (255, 0, 0), button_fila4)
            pygame.draw.rect(screen, (255, 0, 0), button_fila5)
            pygame.draw.rect(screen, (255, 0, 0), button_fila6)
            dado(n)
            pygame.display.update()
            mainClock.tick(60)






