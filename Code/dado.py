import pygame
imagen1 = pygame.image.load("cara1.png")
imagen2 = pygame.image.load("cara2.png")
imagen3 = pygame.image.load("cara3.png")
imagen4 = pygame.image.load("cara4.png")
imagen5 = pygame.image.load("cara5.png")
imagen6 = pygame.image.load("cara6.png")
def dice(n,screen):
    if n == 1:
        screen.blit(imagen1, (620, 580))
    elif n == 2:
        screen.blit(imagen2, (620, 580))
    elif n == 3:
        screen.blit(imagen3, (620, 580))
    elif n == 4:
        screen.blit(imagen4, (620, 580))
    elif n == 5:
        screen.blit(imagen5, (620, 580))
    elif n == 6:
        screen.blit(imagen6, (620, 580))

def puzzle(enum):
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