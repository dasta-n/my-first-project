import pygame
from pygame.colordict import THECOLORS
pygame.init()
scr=pygame.display.set_mode((1000, 800))
scr.fill(THECOLORS["midnightblue"])
scr_over=False
while not scr_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print(event)
            pygame.quit()
    color1 = 255, 255, 255
    color2 = 0, 0, 0
    color3 = 160, 82, 45
    color4 = 178, 34, 34
    color5 = 145, 34, 34
    color6 = 255, 250, 250
    r = pygame.Rect(425, 225, 150, 30)
    r2 = pygame.Rect(427, 225,30 , 80)
    r3 = pygame.Rect(0, 500, 1000, 400)
    pygame.draw.circle(scr,color1, [500, 200], 75, 0 )
    pygame.draw.circle(scr, color2, [470, 190], 8, 0)
    pygame.draw.line(scr, color2, [480, 210], [500, 220],5 )
    pygame.draw.line(scr, color2, [500, 220], [520, 210], 5)
    pygame.draw.line(scr, color3, [300, 400], [460, 235], 5)
    pygame.draw.line(scr, color3, [530, 235], [690, 400], 5)
    pygame.draw.circle(scr, color2, [530, 190], 8, 0)
    pygame.draw.circle(scr, color1, [500, 325], 100, 0)
    pygame.draw.circle(scr, color1, [500, 450], 125, 0)
    pygame.draw.rect(scr, color5, r2, 0)
    pygame.draw.rect(scr, color4, r, 0)
    pygame.draw.rect(scr, color6, r3, 0)
    pygame.draw.circle(scr, color2, [500, 300], 9, 0)
    pygame.draw.circle(scr, color2, [500, 335], 9, 0)

    pygame.display.update()
quit()