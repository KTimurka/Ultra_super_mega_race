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

def draw_console(screen,obj,actions):
    x0 = 900
    y0 = 400
    pygame.draw.circle(screen,(0,0,0),(x0,y0),100,20)
    pygame.draw.polygon(screen,(0,0,0),
                        [
                            (x0 - 90*cos(-obj.phi*pi/180),y0 - 10 - 90*sin(-obj.phi*pi/180)),
                            (x0 + 90*cos(-obj.phi*pi/180),y0 - 10 + 90*sin(-obj.phi*pi/180)),
                            (x0 + 90 * cos(-obj.phi * pi / 180)-20*sin(-obj.phi*pi/180), y0 - 10 + 20*cos(-obj.phi*pi/180) + 90 * sin(-obj.phi * pi / 180)),
                            (x0 - 90 * cos(-obj.phi * pi / 180)-20*sin(-obj.phi*pi/180), y0 - 10 + 20*cos(-obj.phi*pi/180) - 90 * sin(-obj.phi * pi / 180))
                        ])
    pygame.draw.polygon(screen,(0,0,0),
                        [
                            (x0 - 50 * cos(-obj.phi * pi / 180), y0 - 10 - 50 * sin(-obj.phi * pi / 180)),
                            (x0 + 50 * cos(-obj.phi * pi / 180), y0 - 10 + 50 * sin(-obj.phi * pi / 180)),
                            (x0 - 90 * sin(-obj.phi * pi / 180), y0 + 90 * cos(-obj.phi * pi / 180))
                        ])
    if actions[0] == 1:
        image = pygame.image.load("gas.png")
        new_image = pygame.transform.scale(image,(150,150))
        screen.blit(new_image,(800,500))
