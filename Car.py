class Car:
    def __init__(self, road):
        self.x = (road.par[-1]).centerx
        self.y = (road.par[-1]).centery
        self.angle = 0  # Ориентация машинки относительно осей координат
        self.phi = 0    # Поворот руля
        self.v = 0      # Скорость машинки
        self.fuel = 100 # Запас топлива
        self.score = 0  # Набранные очки
