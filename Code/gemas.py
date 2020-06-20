import pygame
amarillaImg = pygame.image.load('gema amarilla.png')
azulImg = pygame.image.load('gema azul.png')
marronImg = pygame.image.load('gema marron.png')
moradaImg = pygame.image.load('gema morada.png')
rojaImg = pygame.image.load('gema roja.png')
verdeImg = pygame.image.load('gema verde.png')

def GemasJ1(j1, screen):
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

def GemasJ2(j2,screen):
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

def GemasJ3(j3,screen):
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

def GemasJ4(j4,screen):
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
