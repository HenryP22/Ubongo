import pygame, sys
import random
import gemas
from Code import grafo
import jugador
import dado
# Setup pygame/window ---------------------------------------- #
mainClock = pygame.time.Clock()
from pygame.locals import *

pygame.init()
pygame.display.set_caption('Ubongo')
screen = pygame.display.set_mode((1280, 720), 0, 32)
pygame.time.set_timer(pygame.USEREVENT, 1000)
font = pygame.font.SysFont(None, 30)

tableroImg = pygame.image.load('tablero ubongo.png')

amarillaImg = pygame.image.load('gema amarilla.png')
azulImg = pygame.image.load('gema azul.png')
marronImg = pygame.image.load('gema marron.png')
moradaImg = pygame.image.load('gema morada.png')
rojaImg = pygame.image.load('gema roja.png')
verdeImg = pygame.image.load('gema verde.png')

def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)
click = False

#-------------------------------------------------------
od = grafo.Grafo(72)
od.crear()
#-------------------------------------------------------

def Base():
    screen.blit(tableroImg, (0, 0))

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



#-------------------------------------------------------

j1 = jugador.player()
j2 = jugador.player()
j3 = jugador.player()
j4 = jugador.player()


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
        self.tiempo = 60
        self.ronda=1
        self.enJuego = False


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
            button_dado = pygame.Rect(615,580,60,57)
            t=jugador.player()


            if button_fila1.collidepoint((mx, my)):
                if click:
                    if self.fila1 <= 60:
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
                        if self.jugador == 1:
                            t = j1
                        elif self.jugador == 2:
                            t = j2
                        elif self.jugador == 3:
                            t = j3
                        elif self.jugador == 4:
                            t = j4
                        pygame.display.update()
                    else: pass


            if button_fila2.collidepoint((mx, my)):
                if click:
                    if self.fila2 <= 61:
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
                    else: pass


            if button_fila3.collidepoint((mx, my)):
                if click:
                    if self.fila3 <= 62:
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
                    else: pass


            if button_fila4.collidepoint((mx, my)):
                if click:
                    if self.fila4 <= 63:
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
                    else: pass


            if button_fila5.collidepoint((mx, my)):
                if click:
                    if self.fila5 <= 64:
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
                    else: pass

            if button_fila6.collidepoint((mx, my)):
                if click:
                    if self.fila6 <= 65:
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
                    else: pass

            if button_iniciar.collidepoint((mx, my)):
                if click:
                    self.enJuego =True
                    enum = random.randint(1, 6)
                    n = random.randint(1, 6)

            if button_dado.collidepoint((mx,my)):
                if click:
                    dado.puzzle(enum)


            click = False

            for event in pygame.event.get():
                if event.type == pygame.USEREVENT and self.enJuego == True:
                    self.tiempo =self.tiempo-1
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
            gemas.GemasJ1(j1,screen)
            gemas.GemasJ2(j2,screen)
            gemas.GemasJ3(j3,screen)
            gemas.GemasJ4(j4,screen)
            pygame.draw.rect(screen, (255, 0, 0), button_fila1)
            pygame.draw.rect(screen, (255, 0, 0), button_fila2)
            pygame.draw.rect(screen, (255, 0, 0), button_fila3)
            pygame.draw.rect(screen, (255, 0, 0), button_fila4)
            pygame.draw.rect(screen, (255, 0, 0), button_fila5)
            pygame.draw.rect(screen, (255, 0, 0), button_fila6)
            if self.tiempo >0 :
                draw_text(str(self.tiempo), font, (255, 255, 255), screen, 205, 67)
            else:
                draw_text(' se acabó el tiempo ', font, (255, 255, 255), screen, 200, 67)
            draw_text(str(self.ronda), font, (255, 255, 255), screen, 975, 67)
            dado.dice(n, screen)
            pygame.display.update()
            mainClock.tick(60)




