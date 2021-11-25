import pygame

pygame.init()
#FPS = 50
#clock = pygame.time.Clock()
#WIDTH = 800
#HEIGHT = 600
#screen = pygame.display.set_mode((WIDTH, HEIGHT))
#pygame.font.init()
#my_font = pygame.font.SysFont('Comic Sans MS', 30)

class Car:
    def __init__(self, screen:pygame.Surface):
'''
конструктор класса Car. Задает 
'''        
        #self.screen = screen
        self.x = highway.startX  #стартовая позиция определяется -> 
        self.y = highway.startY  # -> объектом класса Highway, как и угол
        self.angle = highway.startAngle #стартовый угол от 0 до 359 градусов
        #0 <=> смотрит вправо, поворот - против часовой стрелки
        self.speed = 0
        self.fuel = 100 # стартовое топливо в машине
        #self.acceleration =
        #self.m =
    def move(self):
        '''
        функция задает движение машинки при нажатии на кнопки WASD
        '''
        if keys[pygame.K_a]:
            self.angle += 1
        elif keys[pygame.K_d]:
            self.angle -= 1
        elif keys[pygame.K_w]:
            self.speed += 1
        elif keys[pygame.K_s]:
            self.speed -= 1
        
