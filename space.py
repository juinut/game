import arcade

from models import Ship,World
 
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
 
class SpaceGameWindow(arcade.Window):
    def __init__(self, width, height):
        super().__init__(width, height)
 
        arcade.set_background_color(arcade.color.BLACK)

        
        self.ship_sprite = arcade.Sprite('images/ship.png')
        self.world = World(width, height)

    def update(self, delta):
        self.world.update(delta)
        self.ship_sprite.set_position(self.world.ship.x, self.world.ship.y)
 
 
    def on_draw(self):
        arcade.start_render()
        self.ship_sprite.draw()


 
 
if __name__ == '__main__':
    window = SpaceGameWindow(SCREEN_WIDTH, SCREEN_HEIGHT)
    arcade.run()