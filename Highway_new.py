import math
import sys

import pygame

'''FPS = 30
t = 12 ######           МАСШТАБ
pygame.font.init()
pygame.init()
screen = pygame.display.set_mode((60*t, 60*t))
screen.fill((0, 0, 0))
clock = pygame.time.Clock()
f1 = pygame.font.SysFont('arial', 56)
text1 = f1.render("Alpha", True,
                  (255, 180, 0))'''
class Highway:
    def __init__(self, screen):
#        self.road = ('0', '1', '2', '3')
        self.par = [('25', '10', '40', '10'),
                    ('40', '30', '10', '50'),
                    ('25', '50', '40', '10'),
                    ('10', '30', '10', '50')]



        
