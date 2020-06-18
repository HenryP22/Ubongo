import pygame

# Initialize the pygame
pygame.init()

#create the screen
screen = pygame.display.set_mode((1280,720))

#Title and Icon
pygame.display.set_caption("Ubongo")
icon = pygame.image.load('ubongo-logo.jpg')
pygame.display.set_icon(icon)

# Inicio
inicioImg = pygame.image.load('Inicio.png')

def inicio():
    screen.blit(inicioImg,(0,0))

# Game loop
running = True
while running:
    # RGB = Red, Green, Blue
    screen.fill((255, 0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    inicio()
    pygame.display.update()

def main_menu():
    while True:

        screen.fill((0, 0, 0))
        #draw_text('main menu', font, (255, 255, 255), screen, 20, 20)

        mx, my = pygame.mouse.get_pos()

        button_1 = pygame.Rect(860, 180, 145, 50)
        button_2 = pygame.Rect(760, 290, 330, 50)
        button_3 = pygame.Rect(825, 390, 205, 50)
        button_4 = pygame.Rect(880, 510, 125, 50)
        if button_1.collidepoint((mx, my)):
            if click:
                game()
        if button_2.collidepoint((mx, my)):
            if click:
                options()
        if button_3.collidepoint((mx, my)):
            if click:
                game()
        if button_4.collidepoint((mx, my)):
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

