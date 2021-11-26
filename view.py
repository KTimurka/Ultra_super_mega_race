import pygame

def draw_car(screen,obj,scaled_image):
    x= obj.x
    y= obj.y
    alpha = obj.angle
    rotated_image = pygame.transform.rotate(scaled_image, alpha)
    screen.blit(rotated_image, (x, y))
