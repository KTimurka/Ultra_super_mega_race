import pygame
<<<<<<< Updated upstream
import numpy as np

=======
import sys
>>>>>>> Stashed changes
from view import *
from Car import *
from model import *
from Highway_new import *
<<<<<<< Updated upstream
from race_menu import *

pygame.init()
screen = pygame.display.set_mode((1000, 700))
screen.fill([255, 255, 255])
clock = pygame.time.Clock()

FPS = 60
<<<<<<< HEAD
<<<<<<< HEAD
RED = (255, 0, 0)
BLACK = (0, 0, 0)
=======
RED = (255,0,0)
BLACK = (0,0,0)
>>>>>>> 5e326a6ae048ef153932acd0e92bd8af9e465ac8
=======
RED = (255,0,0)
BLACK = (0,0,0)
>>>>>>> 5e326a6ae048ef153932acd0e92bd8af9e465ac8
=======

pygame.init()
pygame.font.init()
screen = pygame.display.set_mode((600, 600))
screen.fill([255, 255, 255])
clock = pygame.time.Clock()

FPS = 90
>>>>>>> Stashed changes

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

<<<<<<< HEAD
<<<<<<< HEAD

<<<<<<< Updated upstream
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
money0 = [[600, 80], [740, 80], [560, 130], [740, 450], [520, 630], [70, 630], [140, 450], [60, 350]]
fuel0 = [[670, 275], [350, 670]]
money1 =[[450, 125], [450, 225], [750, 250], [725, 425], [450, 600],
            [475, 425], [425, 500], [425, 625], [200, 670], [125, 650],
            [75, 600], [100, 425], [175, 450], [225, 400], [125, 300],
            [212.5, 225], [212.5, 175], [212.5, 150]]
fuel1 = [[425, 50], [710, 350], [420, 520], [500, 50]]
money2 = [[475, 75], [500, 175], [475, 300], [625, 275], [725, 300],
      [675, 400], [600, 425], [500, 400], [500, 575], [375, 650],
      [300, 625], [300, 500], [325, 400], [175, 425], [75, 400],
      [125, 300], [325, 300], [300, 200], [312.5, 160], [312.5, 140],
      [312.5, 120]]
fuel2 = [[475, 225], [620, 460], [630, 325], [330, 75]]
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

=======
>>>>>>> 5e326a6ae048ef153932acd0e92bd8af9e465ac8
=======
>>>>>>> 5e326a6ae048ef153932acd0e92bd8af9e465ac8
# Используемые картинки в проекте
background = pygame.image.load("menu.jpg")

actions = [0,0,0,0,0] # w = actions[0], s = actions[1], a = actions[2], d = actions[3], p = actions[4]
click = False
=======
car1=Car()
road = Highway(screen)

actions = [0,0,0,0,0] # w = actions[0],
                      #s = actions[1],
                      #a = actions[2],
                      #d = actions[3],
                      #p = actions[4]
>>>>>>> Stashed changes
running = True

number = 0
number = show_menu(number)
<<<<<<< HEAD
<<<<<<< HEAD
road = Highway(screen, list_rects[number], list_items[number], item_num_on_i_map[number])
=======
road = Highway(screen,list[number])
>>>>>>> 5e326a6ae048ef153932acd0e92bd8af9e465ac8
=======
road = Highway(screen,list[number])
>>>>>>> 5e326a6ae048ef153932acd0e92bd8af9e465ac8
car1 = Car(road)

drive = []
if number == 0:
    shadow = np.loadtxt("massive0.txt")
if number == 1:
    shadow = np.loadtxt("massive1.txt")
if number == 2:
    shadow = np.loadtxt("massive2.txt")
<<<<<<< HEAD
<<<<<<< HEAD
time = 0   #Счетчик времени
count = 0 #Счетчик кругов
=======
t = 0
>>>>>>> 5e326a6ae048ef153932acd0e92bd8af9e465ac8
=======
t = 0
>>>>>>> 5e326a6ae048ef153932acd0e92bd8af9e465ac8
pygame.mixer.music.load('ACDC.mp3')
pygame.mixer.music.play(-1)
while running:
    clock.tick(FPS)
<<<<<<< Updated upstream
<<<<<<< HEAD
<<<<<<< HEAD
    time +=1
=======
    t +=1
>>>>>>> 5e326a6ae048ef153932acd0e92bd8af9e465ac8
=======
    t +=1
>>>>>>> 5e326a6ae048ef153932acd0e92bd8af9e465ac8
    for event in pygame.event.get():
=======
    for event in pygame.event.get():            
>>>>>>> Stashed changes
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
<<<<<<< HEAD
<<<<<<< HEAD
    if time%8 == 0:
=======
    if t%10 == 0:
>>>>>>> 5e326a6ae048ef153932acd0e92bd8af9e465ac8
=======
    if t%10 == 0:
>>>>>>> 5e326a6ae048ef153932acd0e92bd8af9e465ac8
        drive.append([x,y,alpha])
    screen.fill((255, 255, 255))
<<<<<<< Updated upstream
    move_car(actions, car1, road)
    count = finish(car1, road, count)
    draw_road(screen, road)
<<<<<<< HEAD
<<<<<<< HEAD
    if time//8 < len(shadow):
        draw_car(screen, shadow[time//8][0],shadow[time//8][1],shadow[time//8][2],BLACK)
=======
    if t//8 < len(shadow):
        draw_car(screen, shadow[t//8][0],shadow[t//8][1],shadow[t//8][2],BLACK)
    draw_car(screen, x, y, alpha, RED)
>>>>>>> 5e326a6ae048ef153932acd0e92bd8af9e465ac8
=======
    if t//8 < len(shadow):
        draw_car(screen, shadow[t//8][0],shadow[t//8][1],shadow[t//8][2],BLACK)
    draw_car(screen, x, y, alpha, RED)
>>>>>>> 5e326a6ae048ef153932acd0e92bd8af9e465ac8
    draw_console(screen,car1,actions)
    draw_coin(screen, number, list_items, item_num_on_i_map)
    draw_fuel(screen, list_items, item_num_on_i_map, number)
    draw_car(screen, x, y, alpha, RED)
  #  game_over_screen(screen, car1, list_items)
=======
    screen.fill((0, 0, 0))
    road.draw()
    move_car(actions, car1)
    draw_car(screen,car1,scaled_image)
    
>>>>>>> Stashed changes
    pygame.display.flip()
np_drive = np.array(drive)
<<<<<<< HEAD
<<<<<<< HEAD
print(count)
=======
>>>>>>> 5e326a6ae048ef153932acd0e92bd8af9e465ac8
=======
>>>>>>> 5e326a6ae048ef153932acd0e92bd8af9e465ac8
if number == 0:
    np.savetxt("massive0.txt", np_drive)
if number == 1:
    np.savetxt("massive1.txt", np_drive)
if number == 2:
    np.savetxt("massive2.txt", np_drive)
