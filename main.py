import pygame
import numpy as np

from view import *
from Car import *
from model import *
from Highway_new import *
from race_menu import *

pygame.init()
screen = pygame.display.set_mode((1000, 700))
screen.fill([255, 255, 255])
clock = pygame.time.Clock()

FPS = 60
RED = (255, 0, 0)
BLACK = (0, 0, 0)

list_rects = [
    [pygame.Rect(50, 50, 700, 100),
        pygame.Rect(650, 150, 100, 400),
        pygame.Rect(50, 550, 700, 100),
        pygame.Rect(50, 150, 100, 400),
        pygame.Rect(50, 350, 100, 20)],
    [pygame.Rect(175, 25, 300, 75),
        pygame.Rect(400, 100, 75, 250),
        pygame.Rect(475, 275, 300, 75),
        pygame.Rect(700, 300, 75, 175),
        pygame.Rect(400, 400, 300, 75),
        pygame.Rect(400, 475, 75, 200),
        pygame.Rect(25, 600, 375, 75),
        pygame.Rect(25, 475, 75, 125),
        pygame.Rect(25, 400, 150, 75),
        pygame.Rect(175, 100, 75, 375),
        pygame.Rect(175,100,75,20)],
    [pygame.Rect(275, 25, 250, 75),
        pygame.Rect(450, 100, 75, 150),
        pygame.Rect(450, 250, 300, 75),
        pygame.Rect(675, 325, 75, 50),
        pygame.Rect(450, 375, 300, 75),
        pygame.Rect(450, 450, 75, 150),
        pygame.Rect(275, 600, 250, 75),
        pygame.Rect(275, 450, 75, 150),
        pygame.Rect(50, 375, 300, 75),
        pygame.Rect(50, 325, 75, 50),
        pygame.Rect(50, 250, 300, 75),
        pygame.Rect(275, 100, 75, 150),
        pygame.Rect(275,100,75,20)]
]


item_num_on_i_map = [[8, 2], [18, 4], [21, 4]]
#money = [[[600, 80], [740, 80], [560, 130], [740, 450], [520, 630], [70, 630], [140, 450], [60, 350]],
#         [[450, 125], [450, 225], [750, 250], [725, 425], [450, 600],
#         [475, 425], [425, 500], [425, 625], [200, 670], [125, 650],
#         [75, 600], [100, 425], [175, 450], [225, 400], [125, 300],
#         [212.5, 225], [212.5, 175], [212.5, 150]],
#         [[475, 75], [500, 175], [475, 300], [625, 275], [725, 300],
#      [675, 400], [600, 425], [500, 400], [500, 575], [375, 650],
#      [300, 625], [300, 500], [325, 400], [175, 425], [75, 400],
#      [125, 300], [325, 300], [300, 200], [312.5, 160], [312.5, 140],
#      [312.5, 120]]]
#fuel = [[[670, 275], [350, 670]],
#        [[425, 50], [710, 350], [420, 520], [500, 50]],
#        [[475, 225], [620, 460], [630, 325], [330, 75]]]
money0 = [[600, 80, 1], [740, 80, 1], [560, 130, 1], [740, 450, 1], [520, 630, 1], [70, 630, 1], [140, 450, 1], [60, 350, 1]]
fuel0 = [[670, 275], [350, 570]]
money1 =[[450, 125, 1], [450, 225, 1], [750, 300, 1], [725, 425, 1], [600, 450, 1],
            [475, 425, 1], [425, 500, 1], [425, 625, 1], [200, 670, 1], [125, 650, 1],
            [75, 600, 1], [100, 425, 1], [175, 450, 1], [225, 400, 1], [225, 300, 1],
            [212.5, 225, 1], [212.5, 175, 1], [212.5, 150, 1]]
fuel1 = [[425, 50], [710, 350], [420, 520], [50, 500]]
money2 = [[475, 75, 1], [500, 175, 1], [475, 300, 1], [625, 275, 1], [725, 300, 1],
      [675, 400, 1], [600, 425, 1], [500, 400, 1], [500, 575, 1], [375, 650, 1],
      [300, 625, 1], [300, 500, 1], [325, 400, 1], [175, 425, 1], [75, 400, 1],
      [125, 300, 1], [325, 300, 1], [300, 230, 1], [312.5, 190, 1], [312.5, 170, 1],
      [312.5, 150, 1]]
fuel2 = [[475, 225], [620, 425], [325, 630], [75, 330]]
list_items =[[money0, fuel0], [money1, fuel1],[money2, fuel2]]
    ############# списочек монет и канистр соответственно
    # для первой карты 10 + 4
    
   # [[ (, ), (, ), (, ), (, ), (, ),
   #   (, ), (, ), (, ), (, ), (, )
   #     ],
    #[(, ), (, ), (, ), (, )]]

    ############# для второй карты 18 + 4
    
           

    ############# для третьей карты 21 + 5
    
  
     
     ###########
     

number = 1 ##########################  Number  ---  Должно присваиваться в соответствии
           ########################## с выбранной картой!

# Используемые картинки в проекте
background = pygame.image.load("menu.jpg")
wheel = pygame.image.load("rule.jpg")

actions = [0,0,0,0,0] # w = actions[0], s = actions[1], a = actions[2], d = actions[3], p = actions[4]
click = False
running = True

number = 0
number = show_menu(number)
road = Highway(screen, list_rects[number], list_items[number], item_num_on_i_map[number])
car1 = Car(road)

drive = []
if number == 0:
    shadow = np.loadtxt("massive0.txt")
if number == 1:
    shadow = np.loadtxt("massive1.txt")
if number == 2:
    shadow = np.loadtxt("massive2.txt")
time = 0   #Счетчик времени
count = 0 #Счетчик кругов
pygame.mixer.music.load('ACDC.mp3')
pygame.mixer.music.play(-1)
f1 = pygame.font.Font(None, 36)
while running:
    clock.tick(FPS)
    time +=1
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_a:
            actions[2] = 1
        if event.type == pygame.KEYUP and event.key == pygame.K_a:
            actions[2] = 0
        if event.type == pygame.KEYDOWN and event.key == pygame.K_d:
            actions[3] = 1
        if event.type == pygame.KEYUP and event.key == pygame.K_d:
            actions[3] = 0
        if event.type == pygame.KEYDOWN and event.key == pygame.K_w:
            actions[0] = 1
        if event.type == pygame.KEYUP and event.key == pygame.K_w:
            actions[0] = 0
        if event.type == pygame.KEYDOWN and event.key == pygame.K_s:
            actions[1] = 1
        if event.type == pygame.KEYUP and event.key == pygame.K_s:
            actions[1] = 0
        if pygame.key.get_pressed()[pygame.K_p]:
            actions[4] = 1
    x = car1.x
    y = car1.y
    alpha = -car1.angle*pi/180
    if time%8 == 0:
        drive.append([x,y,alpha])
    screen.fill((255, 255, 255))
    move_car(actions, car1, road)
    count = finish(car1, road, count)
    if count == 3:
        running = False
    draw_road(screen, road)
    if time//8 < len(shadow):
        draw_car(screen, shadow[time//8][0],shadow[time//8][1],shadow[time//8][2],BLACK)
    draw_console(screen,car1,actions,count, f1)
    draw_coin(screen, number, list_items, item_num_on_i_map)
    collect_coin(car1,number,item_num_on_i_map, list_items)
    draw_fuel(screen, list_items, item_num_on_i_map, number)
    draw_car(screen, x, y, alpha, RED)
    game_over_screen(screen, car1, running, time)
    pygame.display.flip()
np_drive = np.array(drive)
best = np.loadtxt("time.txt")
if number == 0 and count == 3 and time<best[0]:
    np.savetxt("massive0.txt", np_drive)
    new_best = np.array([time,best[1],best[2]])
    np.savetxt("time.txt", new_best)
if number == 1 and count == 3 and time<best[1]:
    np.savetxt("massive1.txt", np_drive)
    new_best = np.array([best[0], time, best[2]])
    np.savetxt("time.txt", new_best)
if number == 2 and count == 3 and time<best[2]:
    np.savetxt("massive2.txt", np_drive)
    new_best = np.array([best[0], best[1], time])
    np.savetxt("time.txt", new_best)
