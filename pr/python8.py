'''import pygame

pygame.init()
scr=pygame.display.set_mode((1000, 800))
scr_over=False
while not scr_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print(event)
            pygame.quit()
    r = pygame.Rect(150, 100, 200, 200)
    b = pygame.Rect(220, 200, 70, 100)
    g = pygame.Rect(250, 120, 50, 50 )
    color = 255, 0, 0
    pygame.draw.rect(scr, color, r, 0)
    color1 = 128, 0, 0
    pygame.draw.rect(scr,color1,b,0)
    color2 = 255, 170, 40
    pygame.draw.rect(scr, color2, g, 0)
    color3 = 139, 69, 19
    color4 = 255, 255, 0
    color5 = 0, 0, 0
    pygame.draw.line(scr,color3,[250, 10], [150, 100], width=10)
    pygame.draw.line(scr, color3, [250, 10], [349, 100], width=10)
    pygame.draw.circle(scr, color4, [700, 400], 200, width=0)
    pygame.draw.ellipse(scr, color5, [725, 325, 150, 50], 0)
    pygame.draw.ellipse(scr, color5, [510, 325, 150, 50], 0)
    pygame.draw.line(scr, color5, [520, 425], [850, 425], width=10)


    pygame.display.update()
quit()'''
