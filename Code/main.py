import pygame
import sys
import Tablero

mainClock = pygame.time.Clock()
from pygame.locals import *

pygame.init()
pygame.display.set_caption('Ubongo')
screen = pygame.display.set_mode((1280, 720), 0, 32)

font = pygame.font.SysFont(None, 20)

inicioImg = pygame.image.load('Inicio.png')
seleccionImg = pygame.image.load('Selección de jugadores.png')
instruccionesImg = pygame.image.load('Instrucciones.png')
creditosImg = pygame.image.load('Creditos.png')

def inicio():
    screen.blit(inicioImg,(0,0))

def seleccion():
    screen.blit(seleccionImg,(0,0))

def instrucciones():
    screen.blit(instruccionesImg, (0,0))

def creditos():
    screen.blit(creditosImg,(0,0))

def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)

Juego=Tablero.TableroUbongo()


click = False


def main_menu():
    while True:


        screen.fill((0, 0, 0))
        #draw_text('main menu', font, (255, 255, 255), screen, 20, 20)

        mx, my = pygame.mouse.get_pos()

        button_jugar = pygame.Rect(860, 180, 145, 50)
        button_instrucciones = pygame.Rect(760, 290, 330, 50)
        button_creditos = pygame.Rect(825, 390, 205, 50)
        button_salir = pygame.Rect(880, 510, 125, 50)
        if button_jugar.collidepoint((mx, my)):
            if click:
                game()
        if button_instrucciones.collidepoint((mx, my)):
            if click:
                instructions()
        if button_creditos.collidepoint((mx, my)):
            if click:
                credits()
        if button_salir.collidepoint((mx, my)):
            if click:
                pygame.quit()
                sys.exit()

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

        inicio()
        pygame.display.update()
        mainClock.tick(60)


def game():

    running = True
    while running:


        screen.fill((0, 0, 0))

        mx, my = pygame.mouse.get_pos()

        button_j2 = pygame.Rect(770, 240, 300, 50)
        button_j3 = pygame.Rect(770, 350, 300, 50)
        button_j4 = pygame.Rect(770, 455, 300, 50)

        if button_j2.collidepoint((mx, my)):
            if click:
                Juego.tablero()
                pass
        if button_j3.collidepoint((mx, my)):
            if click:
                Juego.tablero()
                pass
        if button_j4.collidepoint((mx, my)):
            if click:
                Juego.tablero()
                pass

        pygame.draw.rect(screen, (255, 0, 0), button_j2)
        pygame.draw.rect(screen, ( 255, 0, 0), button_j3)
        pygame.draw.rect(screen, (255, 0, 0), button_j4)

        click = False
        #draw_text('game', font, (255, 255, 255), screen, 20, 20)
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        seleccion()
        pygame.display.update()
        mainClock.tick(60)


def instructions():
    running = True
    while running:
        screen.fill((0, 0, 0))

        draw_text('instructions', font, (255, 255, 255), screen, 20, 20)
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False

        instrucciones()
        pygame.display.update()
        mainClock.tick(60)

def credits():
    running = True
    while running:
        screen.fill((0, 0, 0))

        draw_text('credits', font, (255, 255, 255), screen, 20, 20)
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False

        creditos()
        pygame.display.update()
        mainClock.tick(60)


main_menu()
