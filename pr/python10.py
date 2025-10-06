import random

import pygame


pygame.init()
scr=pygame.display.set_mode((600, 600))
scr_over=False

colors = [(0, 255, 0),
          (255, 0, 0),
          (0, 0, 255)]
font = pygame.font.SysFont('numbers', 25)
RandomNumber = random.randint(0, len(colors) - 1)
while not scr_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print(event)
            pygame.quit()

    for horizon in range(10):
        for vertical in range(10):
            x = vertical * 60
            y = horizon * 60
            numbers = font.render(f'{horizon}{vertical}', True, (255, 255, 255))
            pygame.draw.rect(scr, colors[RandomNumber], (x , y, 40, 40), 3)
            scr.blit(numbers, (x + 12, y + 15))
    pygame.display.update()
quit()
