#import math
import sys
from view import *
import pygame

<<<<<<< Updated upstream
'''FPS = 30
=======
#FPS = 30
>>>>>>> Stashed changes
t = 12 ######           МАСШТАБ
pygame.font.init()
#pygame.init()
screen = pygame.display.set_mode((60*t, 60*t))
#screen.fill((0, 0, 0))
#clock = pygame.time.Clock()
f1 = pygame.font.SysFont('arial', 56)
<<<<<<< Updated upstream
text1 = f1.render("Alpha", True,
                  (255, 180, 0))'''
=======
#text1 = f1.render("Alpha", True,
#                  (255, 180, 0))
>>>>>>> Stashed changes
class Highway:
    def __init__(self, screen, list1, list2, item_num):
#        self.road = ('0', '1', '2', '3')
<<<<<<< Updated upstream
        self.par = list1
        # количество монеток и канистр
        # на каждой карте прописывается заранее
        self.items = list2
        self.item_num = item_num
=======
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
        text1 = f1.render("Alpha", True,
                  (255, 180, 0))
 

#screen.blit(text1, (200, 300))
road = Highway(screen)
#pygame.display.update()
#finished = False
#while not finished:

#    screen.fill((0, 0, 0))
#    screen.blit(text1, (235, 200))
#    road.draw()
#    pygame.display.update()

#    clock.tick(FPS)
#    for event in pygame.event.get():
#        if event.type == pygame.QUIT:
#            finished = True

#pygame.quit()



>>>>>>> Stashed changes

