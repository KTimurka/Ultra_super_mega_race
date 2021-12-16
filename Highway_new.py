import math
import sys
from view import *
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
    def __init__(self, screen, list1, list2, item_num):
#        self.road = ('0', '1', '2', '3')
        self.par = list1
        # количество монеток и канистр
        # на каждой карте прописывается заранее
        self.items = list2
        self.item_num = item_num

