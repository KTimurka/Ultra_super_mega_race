import pygame
from Highway_new import *

display_width = 900
display_height = 650
show = True
pygame.init()

clock = pygame.time.Clock()
display = pygame.display.set_mode((display_width, display_height))


def print_text(message, x, y, font_color=(0, 0, 0), font_type='PingPong.ttf', font_size=30):
    font_type = pygame.font.Font(font_type, font_size)
    text = font_type.render(message, True, font_color)
    display.blit(text, (x, y))


class Button:
    def __init__(self, width, height,type):
        self.width = width
        self.height = height
        self.clr = (255, 0, 0)
        self.type = type



    def draw(self, x, y, message, action=None):
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        if x < mouse[0] < x+self.width:
            if y < mouse[1] < y + self.height:
                pygame.draw.rect(display, self.clr, (x, y, self.width, self.height))
                '''if click[0] == 1 and self.type=='settings':
                    a = show_settings()
                    print(a)
                    return(a)
                elif click[0] == 1 and self.type=='start':
                    return True
                elif click[0] == 1 and self.type=='Map 1':
                    return True
                elif click[0] == 1 and self.type=='Map 2':
                    return True
                elif click[0] == 1 and self.type=='Map 3':
                    return True'''
        print_text(message, x+10, y+10)

    def click(self, x, y, message, action=None):
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        if x < mouse[0] < x + self.width:
            if y < mouse[1] < y + self.height:
                if click[0] == 1:
                    return True

def show_settings():
    menu_bckgr = pygame.image.load('menu.jpg')
    list1 = Button(100, 50,'Map 1')
    list2 = Button(100, 50,'Map 2')
    list3 = Button(100, 50, 'Map 3')
    show_set = True
    number = 0
    while show_set:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        display.blit(menu_bckgr, (0, 0))
        list1.draw(200, 50, 'Map 1')
        list2.draw(200, 100, 'Map 2')
        list3.draw(200, 150, 'Map 3')
        if list1.click(200, 50, 'Map 1'):
            number = 0
            show_set = False
        if list2.click(200, 100, 'Map 2'):
            number = 1
            show_set = False
        if list3.click(200, 150,'Map 3') :
            number = 2
            show_set = False

        pygame.display.update()
        clock.tick(60)
    return number


def show_menu(number):
    menu_bckgr = pygame.image.load('menu.jpg')

    start_btn = Button(100, 50,'start')
    settings_btn = Button(140, 50,'settings')
    show = True
    while show:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        display.blit(menu_bckgr, (0, 0))
        start_btn.draw(50, 50, 'START')
        settings_btn.draw(50, 100, 'SETTINGS')
        if start_btn.click(50, 50, 'START'):
            show = False
        if settings_btn.click(50, 100,'SETTINGS'):
            number = show_settings()
            show = True


        pygame.display.update()
        clock.tick(60)
    return number
<<<<<<< HEAD
<<<<<<< HEAD
=======
=======
>>>>>>> 5e326a6ae048ef153932acd0e92bd8af9e465ac8

>>>>>>> 5e326a6ae048ef153932acd0e92bd8af9e465ac8


