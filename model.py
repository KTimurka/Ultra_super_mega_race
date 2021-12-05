import math

def move_car(actions,obj,t):
    '''
    x,y - координаты центра машинки
    '''
    v = obj.v
    angle = obj.angle
    angle += actions[2] - actions[3]
    if (v+0.01*actions[0] - 0.02*actions[1])**2 <= 1:
        v += 0.01*actions[0] - 0.02*actions[1]
    obj.x += -v*math.sin(angle*3.1415/180)
    obj.y += -v*math.cos(angle*3.1415/180)
    obj.v = v
    obj.angle = angle
    '''x = obj.x
    y = obj.y
    angle = obj.angle
    angle += actions[2]-actions[3]
    y += -actions[0]*math.cos(angle*3.1415/180)+actions[1]*math.cos(angle*3.1415/180)
    x += actions[1]*math.sin(angle*3.1415/180)-actions[0]*math.sin(angle*3.1415/180)
    obj.angle = angle
    obj.x = x
    obj.y = y'''
