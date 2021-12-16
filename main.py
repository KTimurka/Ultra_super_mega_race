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
RED = (255,0,0)
BLACK = (0,0,0)

list = [
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

car1 = Car()
# Используемые картинки в проекте
background = pygame.image.load("menu.jpg")

actions = [0,0,0,0,0] # w = actions[0], s = actions[1], a = actions[2], d = actions[3], p = actions[4]
click = False
running = True

number = 0
number = show_menu(number)
road = Highway(screen,list[number])

drive = []
if number == 0:
    shadow = np.loadtxt("massive0.txt")
if number == 1:
    shadow = np.loadtxt("massive1.txt")
if number == 2:
    shadow = np.loadtxt("massive2.txt")
t = 0
while running:
    clock.tick(FPS)
    t +=1
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
    if t%10 == 0:
        drive.append([x,y,alpha])
    screen.fill((255, 255, 255))
    move_car(actions, car1, road)
    draw_road(screen, road)
    if t//8 < len(shadow):
        draw_car(screen, shadow[t//8][0],shadow[t//8][1],shadow[t//8][2],BLACK)
    draw_car(screen, x, y, alpha, RED)
    draw_console(screen,car1,actions)
    pygame.display.flip()
np_drive = np.array(drive)
if number == 0:
    np.savetxt("massive0.txt", np_drive)
if number == 1:
    np.savetxt("massive1.txt", np_drive)
if number == 2:
    np.savetxt("massive2.txt", np_drive)
