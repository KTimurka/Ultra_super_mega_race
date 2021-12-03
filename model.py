import math

def move_car(actions,obj):
    '''
    x,y - координаты центра машинки
    '''
    x = obj.x
    y = obj.y
    angle = obj.angle
    angle += actions[2]-actions[3]
    y += -actions[0]*math.cos(angle*3.1415/180)+actions[1]*math.cos(angle*3.1415/180)
    x += actions[1]*math.sin(angle*3.1415/180)-actions[0]*math.sin(angle*3.1415/180)
    obj.angle = angle
    obj.x = x
    obj.y = y
