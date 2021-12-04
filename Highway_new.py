import math
import sys

import pygame

FPS = 30
t = 12 ######           МАСШТАБ
pygame.font.init()
pygame.init()
screen = pygame.display.set_mode((60*t, 60*t))
screen.fill((0, 0, 0))
clock = pygame.time.Clock()
f1 = pygame.font.SysFont('arial', 56)
text1 = f1.render("Alpha", True,
                  (255, 180, 0))
class Highway:
    def __init__(self, screen):
#        self.road = ('0', '1', '2', '3')
        self.par = [('25', '10', '40', '10'),
                    ('40', '30', '10', '50'),
                    ('25', '50', '40', '10'),
                    ('10', '30', '10', '50')]
    def draw(self):
        for i in range (4):
            pygame.draw.rect(screen, (255, 255, 255),
                             (
                              t*(int(self.par[i][0]))-t*(int(self.par[i][2])/2),
                              t*(int(self.par[i][1]))-t*(int(self.par[i][3])/2),
                              t*int(self.par[i][2]),
                              t*int(self.par[i][3]))
                             )
 
road = Highway(screen)

screen.blit(text1, (200, 300))

pygame.display.update()
finished = False
while not finished:

    screen.fill((0, 0, 0))
    screen.blit(text1, (235, 200))
    road.draw()
    pygame.display.update()

    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()




        
