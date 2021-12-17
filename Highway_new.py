import math
import sys
from view import *
import pygame

class Highway:
    def __init__(self, screen, list1, list2, item_num):
        self.par = list1            # Присваивает дороге соответствующий массив прямоугольников
        self.items = list2          # положение объектов на каждой карте, прописывается заранее
        self.item_num = item_num    # количество монеток и канистр

