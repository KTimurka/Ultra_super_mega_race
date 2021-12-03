from pygame.draw import *
from math import *

def draw_car(screen,obj,scaled_image):
    s = 7
    x= obj.x
    y= obj.y
    alpha = -obj.angle/60
    #rotated_image = pygame.transform.rotate(scaled_image, alpha)
    #screen.blit(rotated_image, (x, y))
    polygon(screen, (255, 0, 0),
            [(x - s * cos(alpha) - 2 * s * sin(alpha), y - s * sin(alpha) + 2 * s * cos(alpha)),
             (x + s * cos(alpha) - 2 * s * sin(alpha), y + s * sin(alpha) + 2 * s * cos(alpha)),
             (x + s * cos(alpha) + 2 * s * sin(alpha), y + s * sin(alpha) - 2 * s * cos(alpha)),
             (x - s * cos(alpha) + 2 * s * sin(alpha), y - s * sin(alpha) - 2 * s * cos(alpha))])
