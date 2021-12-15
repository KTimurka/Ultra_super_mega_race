import pygame
from math import *

def draw_car(screen,obj):
    s = 7
    x= obj.x
    y= obj.y
    alpha = -obj.angle*pi/180
    pygame.draw.polygon(screen, (255, 0, 0),
            [(x - s * cos(alpha) - 2 * s * sin(alpha), y - s * sin(alpha) + 2 * s * cos(alpha)),
             (x + s * cos(alpha) - 2 * s * sin(alpha), y + s * sin(alpha) + 2 * s * cos(alpha)),
             (x + s * cos(alpha) + 2 * s * sin(alpha), y + s * sin(alpha) - 2 * s * cos(alpha)),
             (x - s * cos(alpha) + 2 * s * sin(alpha), y - s * sin(alpha) - 2 * s * cos(alpha))])

def draw_road(screen, road):
    t = 12
    for element in road.par:
        pygame.draw.rect(screen,(125,125,125),element)
    f1 = pygame.font.SysFont('arial', 56)
    text1 = f1.render("Alpha", True,
                      (255, 180, 0))
    screen.blit(text1, (200, 300))

def draw_console(screen,wheel):

