import pygame

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

car1 = Car()
road = Highway(screen)
t = 0
background = pygame.image.load("menu.jpg")

actions = [0,0,0,0,0] # w = actions[0], s = actions[1], a = actions[2], d = actions[3], p = actions[4]
click = False
running = True

show_menu()
while running:
    clock.tick(FPS)
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
    screen.fill((255, 255, 255))
    move_car(actions, car1, t)
    draw_road(screen, road)
    draw_car(screen,car1)
    pygame.display.flip()

