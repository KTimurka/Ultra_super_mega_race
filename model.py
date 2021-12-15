from math import *

def move_car(actions,obj,t):
    '''
    x,y - координаты центра машинки
    '''
    x = obj.x
    y = obj.y
    v = obj.v
    angle = obj.angle
    phi = obj.phi
    x1 = x - 14*sin(angle*3.1415/180) - v*sin(phi*3.1415/180)
    y1 = y - 14*cos(angle*3.1415/180) - v*cos(phi*3.1415/180)
    angle += v*sin((phi - angle)*3.1415/180)*180/(28*3.1415)
    obj.x = x1 + 14*sin(angle*3.1415/180)
    obj.y = y1 + 14*cos(angle*3.1415/180)
    new_v = v + 0.01*actions[0] - 0.02*actions[1]
    if new_v <= 2 and new_v >=0 :
        obj.v = new_v
    obj.phi = phi + 2*(actions[2] - actions[3])
    obj.angle = angle