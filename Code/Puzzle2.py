import pygame


pygame.init()

plataforma_imagen = pygame.Surface((50, 50))
plataforma_imagen.fill(pygame.Color('white'))
plataforma_imagen2 = pygame.Surface((50, 50))
plataforma_imagen2.fill(pygame.Color('red'))

class Plataforma(pygame.sprite.Sprite):

    def __init__(self, x, y, image):
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect(topleft=(x, y))
def main():
    global x1, y1
    global x2, y2,coords2
    screen = pygame.display.set_mode((1280, 720), 0, 32)
    clock = pygame.time.Clock()

    all_sprites = pygame.sprite.Group()
    forma = pygame.sprite.Group()
    coords = [(200+350, 200+150), (200+350, 150+150),
              (250+350, 250+150), (250+350, 200+150), (250+350, 150+150),(250+350,100+150),
              (300+350, 200+150), (300+350, 150+150),(300+350,100+150),
              (350+350, 200+150), (350+350, 150+150),(350+350,100+150),(350+350,50+150)]
    for x1, y1 in coords:
        plataforma = Plataforma(x1, y1, plataforma_imagen)
        all_sprites.add(plataforma)
        forma.add(plataforma)
    hecho = False
    rectangle = pygame.rect.Rect(200, 250, 50, 50)
    rectangle2 = pygame.rect.Rect(200, 300, 50, 50)
    rectangle3 = pygame.rect.Rect(250, 350, 50, 50)
    rectangle4 = pygame.rect.Rect(250, 300, 50, 50)

    rectangle5 = pygame.rect.Rect(400, 450, 50, 50)
    rectangle6 = pygame.rect.Rect(500, 400, 50, 50)
    rectangle7 = pygame.rect.Rect(450, 400, 50, 50)
    rectangle8 = pygame.rect.Rect(400, 400, 50, 50)
    rectangle8_1 = pygame.rect.Rect(500,350, 50, 50)

    rectangle9 = pygame.rect.Rect(600, 300, 50, 50)
    rectangle10 = pygame.rect.Rect(650, 300, 50, 50)
    rectangle11 = pygame.rect.Rect(600, 350, 50, 50)
    rectangle12 = pygame.rect.Rect(650, 350, 50, 50)

    rectangle_draging = False
    rectangle2_draging = False
    rectangle3_draging = False
    rectangle4_draging = False
    rectangle5_draging = False
    rectangle6_draging = False
    rectangle7_draging = False
    rectangle8_draging = False
    rectangle8_1_draging = False
    rectangle9_draging = False
    rectangle10_draging = False
    rectangle11_draging = False
    rectangle12_draging = False
    while not hecho:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                hecho  = True
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if (rectangle.collidepoint(event.pos) or
                            rectangle2.collidepoint(event.pos) or
                            rectangle3.collidepoint(event.pos) or
                            rectangle4.collidepoint(event.pos)):
                        rectangle_draging = True
                        rectangle2_draging = True
                        rectangle3_draging = True
                        rectangle4_draging = True
                        mouse_x, mouse_y = event.pos
                        offset_x = rectangle.x - mouse_x
                        offset_y = rectangle.y - mouse_y
                        offset_x2 = offset_x
                        offset_y2 = offset_y + 50
                        offset_x3 = offset_x2 + 50
                        offset_y3 = offset_y2
                        offset_x4 = offset_x3
                        offset_y4 = offset_y3 + 50
                    if (rectangle5.collidepoint(event.pos) or
                       rectangle6.collidepoint(event.pos) or
                       rectangle7.collidepoint(event.pos) or
                       rectangle8.collidepoint(event.pos) or
                       rectangle8_1.collidepoint(event.pos)):
                       rectangle5_draging = True
                       rectangle6_draging = True
                       rectangle7_draging = True
                       rectangle8_draging = True
                       rectangle8_1_draging = True
                       mouse_x, mouse_y = event.pos
                       offset_x5 = rectangle5.x - mouse_x
                       offset_y5 = rectangle5.y - mouse_y
                       offset_x6 = offset_x5
                       offset_y6 = offset_y5 - 50
                       offset_x7 = offset_x6 + 50
                       offset_y7 = offset_y6
                       offset_x8 = offset_x7 + 50
                       offset_y8 = offset_y7
                       offset_x8_1 = offset_x8
                       offset_y8_1 = offset_y8 - 50
                    if (rectangle9.collidepoint(event.pos) or
                       rectangle10.collidepoint(event.pos) or
                       rectangle11.collidepoint(event.pos) or
                       rectangle12.collidepoint(event.pos) ):
                       rectangle9_draging = True
                       rectangle10_draging = True
                       rectangle11_draging = True
                       rectangle12_draging = True
                       mouse_x, mouse_y = event.pos
                       offset_x9 = rectangle9.x - mouse_x
                       offset_y9 = rectangle9.y - mouse_y
                       offset_x10 = offset_x9
                       offset_y10 = offset_y9 + 50
                       offset_x11 = offset_x9 + 50
                       offset_y11 = offset_y9
                       offset_x12 = offset_x11
                       offset_y12 = offset_y11 + 50
            elif event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:
                    rectangle_draging = False
                    rectangle2_draging = False
                    rectangle3_draging = False
                    rectangle4_draging = False
                    rectangle5_draging = False
                    rectangle6_draging = False
                    rectangle7_draging = False
                    rectangle8_draging = False
                    rectangle8_1_draging = False
                    rectangle9_draging = False
                    rectangle10_draging = False
                    rectangle11_draging = False
                    rectangle12_draging = False
            elif event.type == pygame.MOUSEMOTION:
                if rectangle_draging:
                    mouse_x, mouse_y = event.pos
                    rectangle.x = mouse_x + offset_x
                    rectangle.y = mouse_y + offset_y
                if rectangle2_draging:
                    mouse_x, mouse_y = event.pos
                    rectangle2.x = mouse_x + offset_x2
                    rectangle2.y = mouse_y + offset_y2
                if rectangle3_draging:
                    mouse_x, mouse_y = event.pos
                    rectangle3.x = mouse_x + offset_x3
                    rectangle3.y = mouse_y + offset_y3
                if rectangle4_draging:
                    mouse_x, mouse_y = event.pos
                    rectangle4.x = mouse_x + offset_x4
                    rectangle4.y = mouse_y + offset_y4
                if rectangle5_draging:
                    mouse_x, mouse_y = event.pos
                    rectangle5.x = mouse_x + offset_x5
                    rectangle5.y = mouse_y + offset_y5
                if rectangle6_draging:
                    mouse_x, mouse_y = event.pos
                    rectangle6.x = mouse_x + offset_x6
                    rectangle6.y = mouse_y + offset_y6
                if rectangle7_draging:
                    mouse_x, mouse_y = event.pos
                    rectangle7.x = mouse_x + offset_x7
                    rectangle7.y = mouse_y + offset_y7
                if rectangle8_draging:
                    mouse_x, mouse_y = event.pos
                    rectangle8.x = mouse_x + offset_x8
                    rectangle8.y = mouse_y + offset_y8
                if rectangle8_1_draging:
                    mouse_x, mouse_y = event.pos
                    rectangle8_1.x = mouse_x + offset_x8_1
                    rectangle8_1.y = mouse_y + offset_y8_1
                if rectangle9_draging:
                    mouse_x, mouse_y = event.pos
                    rectangle9.x = mouse_x + offset_x9
                    rectangle9.y = mouse_y + offset_y9
                if rectangle10_draging:
                    mouse_x, mouse_y = event.pos
                    rectangle10.x = mouse_x + offset_x10
                    rectangle10.y = mouse_y + offset_y10
                if rectangle11_draging:
                    mouse_x, mouse_y = event.pos
                    rectangle11.x = mouse_x + offset_x11
                    rectangle11.y = mouse_y + offset_y11
                if rectangle12_draging:
                    mouse_x, mouse_y = event.pos
                    rectangle12.x = mouse_x + offset_x12
                    rectangle12.y = mouse_y + offset_y12
            if (rectangle.x == 550 and rectangle.y == 300 and
                rectangle11.x == 700 and rectangle11.y == 300 and
                rectangle8_1.x == 700 and rectangle8_1.y == 200):
                hecho = True

        all_sprites.update()
        screen.fill((0, 0, 0))
        all_sprites.draw(screen)
        pygame.draw.rect(screen, (255, 0, 0), rectangle)
        pygame.draw.rect(screen, (255, 0, 0), rectangle2)
        pygame.draw.rect(screen, (255, 0, 0), rectangle3)
        pygame.draw.rect(screen, (255, 0, 0), rectangle4)
        pygame.draw.rect(screen, (255, 0, 0), rectangle5)
        pygame.draw.rect(screen, (255, 0, 0), rectangle6)
        pygame.draw.rect(screen, (255, 0, 0), rectangle7)
        pygame.draw.rect(screen, (255, 0, 0), rectangle8)
        pygame.draw.rect(screen, (255, 0, 0), rectangle8_1)
        pygame.draw.rect(screen, (255, 0, 0), rectangle9)
        pygame.draw.rect(screen, (255, 0, 0), rectangle10)
        pygame.draw.rect(screen, (255, 0, 0), rectangle11)
        pygame.draw.rect(screen, (255, 0, 0), rectangle12)
        pygame.display.flip()
        clock.tick(30)

if __name__ == '__main__':
    main()
    pygame.quit()