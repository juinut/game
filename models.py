class Ship:
    def __init__(self, world, x, y):
        self.world = world
        self.x = x
        self.y = y
 
    def update(self, delta):
        if self.y > self.world.height:
            self.y = 0
        self.y += 5

class World:
    def __init__(self, width, height):
        self.width = width
        self.height = height
 
        self.ship = Ship(self, 100, 100)
 
 
    def update(self, delta):
        self.ship.update(delta)