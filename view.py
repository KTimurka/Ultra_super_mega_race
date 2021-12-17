import pygame
from math import *

def draw_car(screen,x,y,alpha,color):
    s = 7
    pygame.draw.polygon(screen, color,
            [(x - s * cos(alpha) - 2 * s * sin(alpha), y - s * sin(alpha) + 2 * s * cos(alpha)),
             (x + s * cos(alpha) - 2 * s * sin(alpha), y + s * sin(alpha) + 2 * s * cos(alpha)),
             (x + s * cos(alpha) + 2 * s * sin(alpha), y + s * sin(alpha) - 2 * s * cos(alpha)),
             (x - s * cos(alpha) + 2 * s * sin(alpha), y - s * sin(alpha) - 2 * s * cos(alpha))])

def draw_road(screen, road):
    t = 12
    for element in road.par:
        pygame.draw.rect(screen,(125,125,125),element)
    pygame.draw.rect(screen, (0, 0, 0), road.par[-1])
    f1 = pygame.font.SysFont('arial', 56)
    text1 = f1.render("Alpha", True,
                      (255, 180, 0))
    screen.blit(text1, (200, 300))

def draw_console(screen,obj,actions, count, f1,time):
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
    text1 = f1.render('Circle: ' + str(count), True, (0, 0, 0))
    text2 = f1.render('Time: ' + str(time//60), True, (0,0,0))
    screen.blit(text1, (800, 50))
    screen.blit(text2, (800, 100))
    pygame.draw.rect(screen,(255,0,0),(800,150,1.5*obj.fuel,20))


def draw_coin (screen, number, list_items, item_num_on_i_map):
    for i in range (item_num_on_i_map[number][0]):
        if list_items[number][0][i][2] == 1:
            pygame.draw.circle(screen, (255, 215, 0), (list_items[number][0][i][0], list_items[number][0][i][1]), 5)

def draw_fuel (screen, list_items, item_num_on_i_map, number):
    t = 5
    for i in range (item_num_on_i_map[number][1]):
        x = list_items[number][1][i][0]          # индексы означают:
        y = list_items[number][1][i][1]          # number - номер карты 
                                               # [0 / 1] - монетка или топливо
                                               # [i] - порядковый номер монетки,
                                               # ее координаты по-отдельности
        pygame.draw.polygon(screen, (255, 0, 0),
                            [(x, y),
                            (x+2*t, y),
                            (x+3*t, y+t),
                            (x+3*t, y+3*t),
                            (x, y+3*t)])
        pygame.draw.polygon(screen, (0, 0, 0),
                            [(x+2.25*t, y+0.25*t),
                            (x+2.75*t, y),
                            (x+2.25*t, y+0.25*t),
                            (x+3*t, y+3*t),
                            (x, y+3*t)])
        pygame.draw.rect(screen, (255, 255, 255), (x+0.5*t, y+0.5*t, 1.2*t, 0.7*t))
        
def collect_coin(obj, number, item_num_on_i_map, list_items):
    for i in range (item_num_on_i_map[number][0]):
        if (abs(obj.x - list_items[number][0][i][0]) +
           abs(obj.y - list_items[number][0][i][1]) < 21) and (list_items[number][0][i][2] == 1):
               obj.score += 1
               list_items[number][0][i][2] = 0

def game_over_screen (screen, obj, running, time, count):
    if obj.fuel <= 0:
        screen.fill((0, 0, 0))
        
        f1 = pygame.font.SysFont('arial', 72)
        text1 = f1.render("Game over", True,
                      (255, 0, 0))
        screen.blit(text1, (100, 250))
        
        f2 = pygame.font.SysFont('arial', 48)
        text2 = f2.render("Out of fuel", True,
                      (255, 0, 0))
        screen.blit(text2, (100, 400))

        f3 = pygame.font.SysFont('arial', 36)
        text3 = f3.render("Your result " + obj.score, True,
                      (255, 0, 0))
        screen.blit(text3, (100, 550))
    if not(running):
        start = True
        while start:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
            screen.fill((0, 0, 0))

            f1 = pygame.font.SysFont('arial', 72)
            text1 = f1.render("You Finished! Congratulations!", True,
                          (255, 255, 255))
            screen.blit(text1, (100, 150))
            f2 = pygame.font.SysFont('arial', 48)
            text2 = f2.render("Time: " + str(time//60), True,
                              (255, 255, 255))
            screen.blit(text2, (100, 400))
            f3 = pygame.font.SysFont('arial', 48)
            text3 = f3.render("Your result " + str(obj.score), True,
                              (255, 255, 255))
            screen.blit(text3, (100, 550))
            pygame.display.update()
