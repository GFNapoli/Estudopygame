import pygame, sys
from pygame.locals import *

windowSurface = pygame.display.set_mode((700, 500))

## Colors list

BLACK = (0, 0, 0)
GRAY = (128, 128, 128)
LIGHT_GRAY = (170, 170, 170)
INDIGO = (75, 0, 130)
DARK_CLAY = (0, 139, 139)
SEA_GREEN = (143, 188, 143)
DARK_GREEN = (0, 100, 0)
BROWN = (139, 69, 19)
ORANGE = (255, 165, 0)
ORANGE_RED = (255, 69, 0)
PINK = (255, 20, 147)
PURPLE = (128, 0, 128)
LIGHT_SKY_BLUE = (135, 206, 250)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

pygame.init()

menu_font = pygame.font.Font("freesansbold.ttf", 17)
texto1 = menu_font.render("1", True, (0, 0, 0))
texto2 = menu_font.render("2", True, (0, 0, 0))
texto3 = menu_font.render("3", True, (0, 0, 0))
texto4 = menu_font.render("4", True, (0, 0, 0))
texto5 = menu_font.render("5", True, (0, 0, 0))
texto6 = menu_font.render("6", True, (0, 0, 0))
texto7 = menu_font.render("7", True, (0, 0, 0))
textoB = menu_font.render("B", True, (0, 0, 0))
draw = False
brush_type = 1
brush_color = BLACK

menu_rect = pygame.Rect(0, 0, 100, 500)
screen_rect = pygame.Rect(100, 0, 600, 500)
pygame.draw.rect(windowSurface, WHITE, screen_rect)

Black_rect = pygame.Rect(5, 33, 20, 20)
Gray_rect = pygame.Rect(27, 33, 20, 20)
Indigo_rect = pygame.Rect(49, 33, 20, 20)
Dark_Clay_rect = pygame.Rect(71, 33, 20, 20)
Sea_Green_rect = pygame.Rect(5, 55, 20, 20)
Dark_Green_rect = pygame.Rect(27, 55, 20, 20)
Brown_rect = pygame.Rect(49, 55, 20, 20)
Orange_rect = pygame.Rect(71, 55, 20, 20)
Pink_rect = pygame.Rect(5, 77, 20, 20)
Purple_rect = pygame.Rect(27, 77, 20, 20)
Light_Sky_Blue_rect = pygame.Rect(49, 77, 20, 20)
ORANGE_RED_rect = pygame.Rect(71, 77, 20, 20)
Red_rect = pygame.Rect(5, 99, 20, 20)
Green_rect = pygame.Rect(27, 99, 20, 20)
Blue_rect = pygame.Rect(49, 99, 20, 20)
Yellow_rect = pygame.Rect(71, 99, 20, 20)

brush_1 = pygame.Rect(5, 185, 20, 20)
brush_2 = pygame.Rect(27, 185, 20, 20)
brush_3 = pygame.Rect(49, 185, 20, 20)
brush_4 = pygame.Rect(71, 185, 20, 20)
brush_5 = pygame.Rect(5, 207, 20, 20)
brush_6 = pygame.Rect(27, 207, 20, 20)
brush_7 = pygame.Rect(49, 207, 20, 20)
brush_e = pygame.Rect(38, 240, 20, 20)

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                pygame.quit()
                sys.exit()
        if event.type == MOUSEBUTTONDOWN:
            draw = True
        if event.type == MOUSEBUTTONUP:
            draw = False

    # desenha, quando clica
    mouse_pos = pygame.mouse.get_pos()
    if draw == True and mouse_pos[0] > 100:
        pygame.draw.circle(windowSurface, brush_color, mouse_pos, brush_type)

    # detecta cor
    if draw == True:
        if Dark_Clay_rect.collidepoint(mouse_pos):
            brush_color = DARK_CLAY

        if Indigo_rect.collidepoint(mouse_pos):
            brush_color = INDIGO

        if Gray_rect.collidepoint(mouse_pos):
            brush_color = GRAY

        if Black_rect.collidepoint(mouse_pos):
            brush_color = BLACK

        if Sea_Green_rect.collidepoint(mouse_pos):
            brush_color = SEA_GREEN

        if Dark_Green_rect.collidepoint(mouse_pos):
            brush_color = DARK_GREEN

        if Brown_rect.collidepoint(mouse_pos):
            brush_color = BROWN

        if Orange_rect.collidepoint(mouse_pos):
            brush_color = ORANGE

        if Pink_rect.collidepoint(mouse_pos):
            brush_color = PINK

        if Purple_rect.collidepoint(mouse_pos):
            brush_color = PURPLE

        if Light_Sky_Blue_rect.collidepoint(mouse_pos):
            brush_color = LIGHT_SKY_BLUE

        if ORANGE_RED_rect.collidepoint(mouse_pos):
            brush_color = ORANGE_RED

        if Red_rect.collidepoint(mouse_pos):
            brush_color = RED

        if Blue_rect.collidepoint(mouse_pos):
            brush_color = BLUE

        if Green_rect.collidepoint(mouse_pos):
            brush_color = GREEN

        if Yellow_rect.collidepoint(mouse_pos):
            brush_color = YELLOW

    if draw == True:
        if brush_e.collidepoint(mouse_pos):
            brush_color = WHITE

    pygame.draw.rect(windowSurface, LIGHT_GRAY, menu_rect)

    # detecta tamanho do pincel
    if draw == True:
        if brush_1.collidepoint(mouse_pos):
            brush_type = 1
        if brush_2.collidepoint(mouse_pos):
            brush_type = 2
        if brush_3.collidepoint(mouse_pos):
            brush_type = 3
        if brush_4.collidepoint(mouse_pos):
            brush_type = 4
        if brush_5.collidepoint(mouse_pos):
            brush_type = 5
        if brush_6.collidepoint(mouse_pos):
            brush_type = 6
        if brush_7.collidepoint(mouse_pos):
            brush_type = 7

    # reage ao selecionar as cores
    pygame.draw.rect(windowSurface, BLACK, Black_rect)
    if brush_color == BLACK:
        border = 3
    else:
        border = 1
    pygame.draw.rect(windowSurface, BLACK, Black_rect, border)

    pygame.draw.rect(windowSurface, GRAY, Gray_rect)
    if brush_color == GRAY:
        border = 3
    else:
        border = 1
    pygame.draw.rect(windowSurface, BLACK, Gray_rect, border)

    pygame.draw.rect(windowSurface, DARK_CLAY, Dark_Clay_rect)
    if brush_color == DARK_CLAY:
        border = 3
    else:
        border = 1
    pygame.draw.rect(windowSurface, BLACK, Dark_Clay_rect, border)

    pygame.draw.rect(windowSurface, INDIGO, Indigo_rect)
    if brush_color == INDIGO:
        border = 3
    else:
        border = 1
    pygame.draw.rect(windowSurface, BLACK, Indigo_rect, border)

    pygame.draw.rect(windowSurface, SEA_GREEN, Sea_Green_rect)
    if brush_color == SEA_GREEN:
        border = 3
    else:
        border = 1
    pygame.draw.rect(windowSurface, BLACK, Sea_Green_rect, border)

    pygame.draw.rect(windowSurface, DARK_GREEN, Dark_Green_rect)
    if brush_color == DARK_GREEN:
        border = 3
    else:
        border = 1
    pygame.draw.rect(windowSurface, BLACK, Dark_Green_rect, border)

    pygame.draw.rect(windowSurface, BROWN, Brown_rect)
    if brush_color == BROWN:
        border = 3
    else:
        border = 1
    pygame.draw.rect(windowSurface, BLACK, Brown_rect, border)

    pygame.draw.rect(windowSurface, ORANGE, Orange_rect)
    if brush_color == ORANGE:
        border = 3
    else:
        border = 1
    pygame.draw.rect(windowSurface, BLACK, Orange_rect, border)

    pygame.draw.rect(windowSurface, PINK, Pink_rect)
    if brush_color == PINK:
        border = 3
    else:
        border = 1
    pygame.draw.rect(windowSurface, BLACK, Pink_rect, border)

    pygame.draw.rect(windowSurface, PURPLE, Purple_rect)
    if brush_color == PURPLE:
        border = 3
    else:
        border = 1
    pygame.draw.rect(windowSurface, BLACK, Purple_rect, border)

    pygame.draw.rect(windowSurface, LIGHT_SKY_BLUE, Light_Sky_Blue_rect)
    if brush_color == LIGHT_SKY_BLUE:
        border = 3
    else:
        border = 1
    pygame.draw.rect(windowSurface, BLACK, Light_Sky_Blue_rect, border)

    pygame.draw.rect(windowSurface, RED, Red_rect)
    if brush_color == RED:
        border = 3
    else:
        border = 1
    pygame.draw.rect(windowSurface, BLACK, Red_rect, border)

    pygame.draw.rect(windowSurface, ORANGE_RED, ORANGE_RED_rect)
    if brush_color == ORANGE_RED:
        border = 3
    else:
        border = 1
    pygame.draw.rect(windowSurface, BLACK, ORANGE_RED_rect, border)

    pygame.draw.rect(windowSurface, BLUE, Blue_rect)
    if brush_color == BLUE:
        border = 3
    else:
        border = 1
    pygame.draw.rect(windowSurface, BLACK, Blue_rect, border)

    pygame.draw.rect(windowSurface, GREEN, Green_rect)
    if brush_color == GREEN:
        border = 3
    else:
        border = 1
    pygame.draw.rect(windowSurface, BLACK, Green_rect, border)

    pygame.draw.rect(windowSurface, YELLOW, Yellow_rect)
    if brush_color == YELLOW:
        border = 3
    else:
        border = 1
    pygame.draw.rect(windowSurface, BLACK, Yellow_rect, border)

    # reage ao selecionar o pincel

    if brush_type == 1:
        brush_border = 3
    else:
        brush_border = 1
    pygame.draw.rect(windowSurface, BLACK, brush_1, brush_border)
    windowSurface.blit(texto1, (11, 188))
    pygame.draw.rect(windowSurface, BLACK, brush_1, brush_border)

    if brush_type == 2:
        brush_border = 3
    else:
        brush_border = 1
    pygame.draw.rect(windowSurface, BLACK, brush_2, brush_border)
    windowSurface.blit(texto2, (33, 188))
    pygame.draw.rect(windowSurface, BLACK, brush_2, brush_border)

    if brush_type == 3:
        brush_border = 3
    else:
        brush_border = 1
    pygame.draw.rect(windowSurface, BLACK, brush_3, 1)
    windowSurface.blit(texto3, (55, 188))
    pygame.draw.rect(windowSurface, BLACK, brush_3, brush_border)

    if brush_type == 4:
        brush_border = 3
    else:
        brush_border = 1
    pygame.draw.rect(windowSurface, BLACK, brush_4, brush_border)
    windowSurface.blit(texto4, (77, 188))
    pygame.draw.rect(windowSurface, BLACK, brush_4, brush_border)

    if brush_type == 5:
        brush_border = 3
    else:
        brush_border = 1
    pygame.draw.rect(windowSurface, BLACK, brush_5, brush_border)
    windowSurface.blit(texto5, (11, 210))
    pygame.draw.rect(windowSurface, BLACK, brush_5, brush_border)

    if brush_type == 6:
        brush_border = 3
    else:
        brush_border = 1
    pygame.draw.rect(windowSurface, BLACK, brush_6, brush_border)
    windowSurface.blit(texto6, (33, 210))
    pygame.draw.rect(windowSurface, BLACK, brush_6, brush_border)

    if brush_type == 7:
        brush_border = 3
    else:
        brush_border = 1
    pygame.draw.rect(windowSurface, BLACK, brush_7, brush_border)
    windowSurface.blit(texto7, (55, 210))
    pygame.draw.rect(windowSurface, BLACK, brush_7, brush_border)

    windowSurface.blit(textoB, (42,243))
    if brush_color == WHITE:
        border = 3
    else:
        border = 1
    pygame.draw.rect(windowSurface, BLACK, brush_e, border)

    pygame.display.update()
