class Ship:
    def __init__(self, x, y):
        self.x = x
        self.y = y
 
    def update(self, delta):
        if self.y > 600:
            self.y = 0
        self.y += 5