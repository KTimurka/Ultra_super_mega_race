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

# Параметры отрисовки
FPS = 60
RED = (255, 0, 0)
BLACK = (0, 0, 0)

# ВНИМАНИЕ!!! Дальше 50 строк захардкоженных дорог. Берегите ваши глаза)
# Спасибо за понимание! :)
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
money0 = [
            [600, 80, 1], [740, 80, 1], [560, 130, 1], [740, 450, 1], [520, 630, 1],
            [70, 630, 1], [140, 450, 1], [60, 350, 1]
          ]
fuel0 = [[670, 275,1], [350, 570,1]]
money1 =[
            [450, 125, 1], [450, 225, 1], [750, 300, 1], [725, 425, 1], [600, 450, 1],
            [475, 425, 1], [425, 500, 1], [425, 625, 1], [200, 670, 1], [125, 650, 1],
            [75, 600, 1], [100, 425, 1], [175, 450, 1], [225, 400, 1], [225, 300, 1],
            [212.5, 225, 1], [212.5, 175, 1], [212.5, 150, 1]
         ]
fuel1 = [[425, 50,1], [710, 350,1], [420, 520,1], [50, 500,1]]
money2 = [
            [475, 75, 1], [500, 175, 1], [475, 300, 1], [625, 275, 1], [725, 300, 1],
            [675, 400, 1], [600, 425, 1], [500, 400, 1], [500, 575, 1], [375, 650, 1],
            [300, 625, 1], [300, 500, 1], [325, 400, 1], [175, 425, 1], [75, 400, 1],
            [125, 300, 1], [325, 300, 1], [300, 230, 1], [312.5, 190, 1], [312.5, 170, 1],
            [312.5, 150, 1]
        ]
fuel2 = [[475, 225,1], [620, 425,1], [325, 630,1], [75, 330,1]]
list_items =[[money0, fuel0], [money1, fuel1],[money2, fuel2]]
# Уже можно открывать глаза...

# Используемые картинки в проекте
background = pygame.image.load("menu.jpg")

# Инициализация переменных
number = 0              # Номер выбранной карты - 1
time = 0                # Счетчик времени
count = 0               # Счетчик кругов
running = True          # Флаг
actions = [0,0,0,0]     # w = actions[0], s = actions[1], a = actions[2], d = actions[3]

# Создание игровых объектов
number = show_menu(number)
road = Highway(screen, list_rects[number], list_items[number], item_num_on_i_map[number])
car1 = Car(road)

# Массив, куда будем записывать координаты "тени"
drive = []

# Запуск "тени" для соответствующей карты
if number == 0:
    shadow = np.loadtxt("massive0.txt")
if number == 1:
    shadow = np.loadtxt("massive1.txt")
if number == 2:
    shadow = np.loadtxt("massive2.txt")

# Музыка и шрифт
pygame.mixer.music.load('ACDC.mp3')
pygame.mixer.music.play(-1)
f1 = pygame.font.Font(None, 36)

while running:
    clock.tick(FPS)
    time +=1
    for event in pygame.event.get():

        # Диспетчеризация событий с клавиатуры
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

    # Запись "Тени" машинки
    x = car1.x
    y = car1.y
    alpha = -car1.angle*pi/180
    if time%5 == 0:
        drive.append([x,y,alpha])

    # Обработка событий с объектами
    move_car(actions, car1, road)
    collect_coin(car1, number, item_num_on_i_map, list_items)
    collect_fuel(car1, number, item_num_on_i_map, list_items)
    if finish(car1, road):
        count+=1
    if count == 3:
        running = False

    # Блок отрисовки всех элементов
    screen.fill((255, 255, 255))
    draw_road(screen, road, number)
    if time//5 < len(shadow):
        draw_car(screen, shadow[time//5][0],shadow[time//5][1],shadow[time//5][2],BLACK)
    draw_coin(screen, number, list_items, item_num_on_i_map)
    draw_fuel(screen, list_items, item_num_on_i_map, number, road, car1)
    draw_car(screen, x, y, alpha, RED)
    draw_console(screen, car1, actions, count, f1, time)

    # Проверка, не закончилась ли игра
    game_over_screen(screen, car1, running, time, count)
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
