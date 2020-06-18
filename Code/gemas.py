import pygame, sys

# Setup pygame/window ---------------------------------------- #
mainClock = pygame.time.Clock()
from pygame.locals import *

pygame.init()
pygame.display.set_caption('Ubongo')
screen = pygame.display.set_mode((1280, 720), 0, 32)

font = pygame.font.SysFont(None, 20)

tableroImg = pygame.image.load('tablero ubongo.png')
def tabla():
    screen.blit(tableroImg,(0,0))

verdeImg = pygame.image.load('gema verde.png')
rojaImg = pygame.image.load('gema roja.png')
moradaImg = pygame.image.load('gema morada.png')
marronImg = pygame.image.load('gema marron.png')
azulImg = pygame.image.load('gema azul.png')
amarillaImg = pygame.image.load('gema amarilla.png')

def verde():
    x = 425
    y=100
    for i in range (6):
        for j in range(12):
            screen.blit(verdeImg,(x,y))
            if(j<3):
                x = x + 62
            if (j>=3):
                x= x+ 63
        x = 425
        y = y + 51

def roja():
    screen.blit(rojaImg,(0,0))

def morada():
    screen.blit(moradaImg,(0,0))

def marron():
    screen.blit(marronImg,(0,0))

def azul():
    screen.blit(azulImg,(0,0))

def amarrilla():
    screen.blit(amarillaImg,(0,0))

tableroImg = pygame.image.load('tablero ubongo.png')
def tabla():
    screen.blit(tableroImg,(0,0))

verde()

click = False


def main_menu():
    while True:


        screen.fill((0, 0, 0))
        #draw_text('main menu', font, (255, 255, 255), screen, 20, 20)

        mx, my = pygame.mouse.get_pos()


        #pygame.draw.rect(screen, (255, 0, 0), button_1)
        #pygame.draw.rect(screen, (255, 0, 0), button_2)
        #pygame.draw.rect(screen, (255, 0, 0), button_3)
        #pygame.draw.rect(screen, (255, 0, 0), button_4)

        click = False
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True


        tabla()
        verde()
        pygame.display.update()
        mainClock.tick(60)

main_menu()