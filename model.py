from math import *
import pygame

def move_car(actions,obj,road):
    '''
    x,y - координаты центра машинки
    '''
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
<<<<<<< HEAD

def finish(car,road,count):
    if (road.par[-1]).collidepoint(car.x,car.y):
        if car.v*cos(-car.angle*pi/180) > 0:
            count += 1
    return(count)

    obj.fuel -= 0.05
        
    

    
=======
def finish(car,road):
    count = 0
    if road.par[-1].collidepoint(car.x,car.y) == -1:
        pass
>>>>>>> 5e326a6ae048ef153932acd0e92bd8af9e465ac8
