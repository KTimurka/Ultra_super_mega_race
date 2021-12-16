class Car:
    def __init__(self, road):
        self.x = (road.par[-1]).centerx
        self.y = (road.par[-1]).centery
        self.angle = 0
        self.phi = 0
        self.omega = 6
        self.v = 0
        
        self.fuel = 100
        self.score = 0
