import pygame
from math import *
from model import *

def draw_car(screen,x,y,alpha,color):
    '''Рисует машинку (прямоугольник). Учитывает где ее центр и угол поворота.'''
    s = 7
    pygame.draw.polygon(screen, color,
            [(x - s * cos(alpha) - 2 * s * sin(alpha), y - s * sin(alpha) + 2 * s * cos(alpha)),
             (x + s * cos(alpha) - 2 * s * sin(alpha), y + s * sin(alpha) + 2 * s * cos(alpha)),
             (x + s * cos(alpha) + 2 * s * sin(alpha), y + s * sin(alpha) - 2 * s * cos(alpha)),
             (x - s * cos(alpha) + 2 * s * sin(alpha), y - s * sin(alpha) - 2 * s * cos(alpha))])


def draw_road(screen, road, number):
    '''Рисует дороги. Получает на вход дорогу(массив прямоугольников), а также номер карты.'''
    t = 12
    for element in road.par:
        pygame.draw.rect(screen,(125,125,125),element)
    pygame.draw.rect(screen, (0, 0, 0), road.par[-1])
    names = ["Alpha", "Bravo", "Charlie"]
    f = pygame.font.SysFont('arial', 56)
    text = f.render(names[number], True,
                      (255, 180, 0))
    if number == 0:
        screen.blit(text, (200, 300))
    elif number == 1:
        screen.blit(text, (25, 25))
    elif number == 2:
        screen.blit(text, (25, 25))


def draw_console(screen,obj,actions, count, f1,time):
    '''Рисует панель управления (руль, топливо, очки, педальку).'''
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
    text1 = f1.render('Circle : ' + str(count), True, (0, 0, 0))
    text2 = f1.render('Time : ' + str(time//60), True, (0,0,0))
    text3 = f1.render('Score : ' + str(obj.score), True, (0, 0, 0))
    screen.blit(text1, (800, 0))
    screen.blit(text2, (800, 50))
    screen.blit(text3, (800, 100))
    pygame.draw.rect(screen,(255,0,0),(800,150,1.5*obj.fuel,20))
    pygame.draw.rect(screen, (0, 0, 0), (800, 150, 150, 20),2)


def draw_coin (screen, number, list_items, item_num_on_i_map):
    '''Рисует еще не собранные монетки в заданных местах карты.'''
    for i in range (item_num_on_i_map[number][0]):
        if list_items[number][0][i][2] == 1:
            pygame.draw.circle(screen, (255, 215, 0), (list_items[number][0][i][0], list_items[number][0][i][1]), 5)


def draw_fuel (screen, list_items, item_num_on_i_map, number,road,obj):
    '''Рисует еще не собранные канистры топлива. Обновляется при пересечении финиша.'''
    t = 5
    for i in range(item_num_on_i_map[number][1]):
        if (list_items[number][1][i][2] == 1) or (finish(obj,road)):
            if finish(obj,road):
                obj.fuel = 100
                list_items[number][1][i][2] = 1
            x = list_items[number][1][i][0]  # индексы означают:
            y = list_items[number][1][i][1]  # number - номер карты
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
                                [(x + 2.25 * t, y + 0.25 * t),
                                 (x + 2.5 * t, y),
                                 (x + 3 * t, y + 0.5 * t),
                                 (x + 2.75 * t, y + 0.75 * t)])
            pygame.draw.rect(screen, (125, 125, 125), (x+0.5*t, y+0.5*t, 1.2*t, 0.7*t))


def game_over_screen (screen, obj, running, time, count):
    '''Запускает окно проигрыша по окончании игры.'''
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
        text3 = f3.render("Your result " + str(obj.score), True,
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
            if count == 3:
                image = pygame.image.load("final_race.jpg")
                new_image = pygame.transform.scale(image, (1000, 700))
                screen.blit(new_image, (0, 0))
                f1 = pygame.font.SysFont('arial', 72)
                text1 = f1.render("You Finished! Congratulations!", True,
                          (255, 255, 255))
                screen.blit(text1, (100, 0))
                f2 = pygame.font.SysFont('arial', 48)
                text2 = f2.render("Time: " + str(time//60), True,
                              (255, 255, 255))
                screen.blit(text2, (100, 400))
                f3 = pygame.font.SysFont('arial', 48)
                text3 = f3.render("Your result: " + str(obj.score), True,
                              (255, 255, 255))
                screen.blit(text3, (100, 500))
            else:
                image = pygame.image.load("family.jpg")
                new_image = pygame.transform.scale(image, (1000, 700))
                screen.blit(new_image, (0, 0))
            pygame.display.update()