from math import *
import pygame

def move_car(actions,obj,road):
    '''
    x,y - координаты центра машинки
    '''
    '''x = obj.x
    y = obj.y
    v = obj.v
    angle = obj.angle
    phi = obj.phi
    x1 = x - 14*sin(angle*3.1415/180) - v*sin((phi)*3.1415/180)
    y1 = y - 14*cos(angle*3.1415/180) - v*cos((phi)*3.1415/180)
    angle += v*sin((phi-angle)*3.1415/180)*180/(28*3.1415)
    obj.x = x1 + 14*sin(angle*3.1415/180)
    obj.y = y1 + 14*cos(angle*3.1415/180)
    new_v = v + 0.01*actions[0] - 0.02*actions[1]
    if new_v <= 2 and new_v >=0 :
        obj.v = new_v
    #check(obj,road)
    obj.phi = phi + (actions[2] - actions[3])
    obj.angle = angle'''
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
    if new_v <= 2 and new_v >= -1:
        obj.v = new_v
    if car.collidelist(road.par) == -1:
        obj.v = obj.v/1.1
    new_phi = phi + (actions[2] - actions[3])
    if new_phi <= 45 and new_phi >= -45:
        obj.phi = phi + (actions[2] - actions[3])
    obj.angle = angle