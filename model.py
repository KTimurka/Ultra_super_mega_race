from math import *
import pygame


def move_car(actions,obj,road):
    '''Функция физично рассчитывает движение машинки и ее повороты.
    Доверьтесь, там все прекрасно :)
    x,y - координаты центра машинки'''
    x = obj.x
    y = obj.y
    v = obj.v
    car = pygame.Rect(x,y,7,14)
    angle = obj.angle
    phi = obj.phi
    x1 = x - 14 * sin(angle * pi / 180) - v * sin((phi + angle) * pi / 180)
    y1 = y - 14 * cos(angle * pi / 180) - v * cos((phi + angle) * pi / 180)
    angle += v * sin(phi * pi / 180) * 180 / (28 * pi)
    obj.x = x1 + 14 * sin(angle * pi / 180)
    obj.y = y1 + 14 * cos(angle * pi / 180)
    new_v = v + 0.01 * actions[0] - 0.02 * actions[1]
    if new_v <= 4 and new_v >= -1:
        obj.v = new_v*(0.998)
    if car.collidelist(road.par) == -1:
        obj.v = obj.v/1.1
    new_phi = phi + (actions[2] - actions[3])
    if new_phi <= 45 and new_phi >= -45:
        obj.phi = phi + (actions[2] - actions[3])
    if obj.phi != 0:
        obj.phi += abs(v) * sin(-phi * 3.1415 / 180) * 180 / (35 * 3.1415)
    obj.angle = angle
    obj.fuel -= 0.08


def finish(car,road):
    '''Функция проверяет пересечение черты финиша. Возвращает True если пересечение было.'''
    y0 = (road.par[-1]).centery
    newy = car.y + car.v*cos(-car.angle*pi/180)
    param = False
    if car.y < y0 and newy > y0:
            param = True
    return(param)


def collect_coin(obj, number, item_num_on_i_map, list_items):
    '''Функция проверяет касание монетки. Обрабатывает сбор и удаляет собранные монетки.'''
    for i in range (item_num_on_i_map[number][0]):
        if (abs(obj.x - list_items[number][0][i][0]) +
           abs(obj.y - list_items[number][0][i][1]) < 21) and (list_items[number][0][i][2] == 1):
               obj.score += 1
               list_items[number][0][i][2] = 0


def collect_fuel(obj, number, item_num_on_i_map, list_items):
    '''Функция проверяет касание топлива. Обрабатывает сбор и удаляет собранное топливо.'''
    for i in range (item_num_on_i_map[number][1]):
        if (abs(obj.x - list_items[number][1][i][0]) +
           abs(obj.y - list_items[number][1][i][1]) < 25) and (list_items[number][1][i][2] == 1):
               obj.fuel = 100
               list_items[number][1][i][2] = 0
        
    

    
