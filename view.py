import pygame
import math

pygame.init()
screen = pygame.display.set_mode((800, 600))
screen.fill([255, 255, 255])
clock = pygame.time.Clock()

car = pygame.image.load("mashina.jpg").convert_alpha()

scaled_image = pygame.transform.scale(car, (50, 100))

angle = 0

x = 50
y = 50
dr = 8   
                    #    if pygame.key.get_pressed()[pygame.K_RIGHT]
                    #    pygame.key.get_pressed()[pygame.K_a]
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif pygame.key.get_pressed()[pygame.K_a]:
                angle -= 1
                angle = angle % 360
        elif pygame.key.get_pressed()[pygame.K_d]:
                angle += 1
                angle = angle % 360
        elif pygame.key.get_pressed()[pygame.K_w]:
                x -= dr*math.cos(angle*3.1415/180)
                y += dr*math.sin(angle*3.1415/180)
        elif pygame.key.get_pressed()[pygame.K_s]:
                x += dr*math.cos(angle*3.1415/180)
                y -= dr*math.sin(angle*3.1415/180)
        elif pygame.key.get_pressed()[pygame.K_p]:
                print(angle, ' ', x, ' ', y )
    # обновляем значения
    # рисуем
    screen.fill((255, 255, 255))
    #screen.blit(car, (0,0))
    #screen.blit(scaled_image, (600, 0))

    # исходное изображение поворачивается на значение переменной angle
    # и записывается в перменную rotated_image
    rotated_image = pygame.transform.rotate(scaled_image, angle)
    screen.blit(rotated_image, (x, y))

    pygame.display.flip()
    clock.tick(200)