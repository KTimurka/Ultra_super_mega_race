import pygame

from view import *
from Car import *
from model import *

pygame.init()
screen = pygame.display.set_mode((800, 600))
screen.fill([255, 255, 255])
clock = pygame.time.Clock()

FPS = 60

car = pygame.image.load('mashina.jpg').convert_alpha()

scaled_image = pygame.transform.scale(car, (50, 100))

car1=Car()

actions = [0,0,0,0,0] # w = actions[0], s = actions[1], a = actions[2], d = actions[3], p = actions[4]
running = True
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
    move_car(actions, car1)
    draw_car(screen,car1,scaled_image)
    pygame.display.flip()

