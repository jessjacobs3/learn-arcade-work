import arcade
import random

# --- Constants ---
SPRITE_SCALING_BOX = 1
SPRITE_SCALING_PLAYER = 0.4
MOVEMENT_SPEED = 5
PLAYER_SCALE = 0.7
COIN_SCALE = 0.35
COIN_COUNT = 30
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600


class Coin(arcade.Sprite):

    def __init__(self, filename, sprite_scaling):

        super().__init__(filename, sprite_scaling)

        self.change_x = 0
        self.change_y = 0

    def update(self):

        self.center_x += self.change_x
        self.center_y += self.change_y

        if self.left < 0:
            self.change_x *= -1

        if self.right > SCREEN_WIDTH:
            self.change_x *= -1

        if self.bottom < 0:
            self.change_y *= -1

        if self.top > SCREEN_HEIGHT:
            self.change_y *= -1

class MyGame(arcade.Window):
    """ This class represents the main window of the game. """

    def __init__(self):
        """ Initializer """
        # Call the parent class initializer
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "Lab 9")
        self.physics_engine = None

        # Sprite Lists
        self.player_list = None
        self.wall_list = None

        # Set up the player
        self.player_sprite = None

        self.camera_for_sprites = arcade.Camera(SCREEN_WIDTH, SCREEN_HEIGHT)
        self.camera_for_gui = arcade.Camera(SCREEN_WIDTH, SCREEN_HEIGHT)

    def setup(self):
        # Set the background color
        arcade.set_background_color(arcade.color.BLUE_SAPPHIRE)

        # Sprite Lists
        self.player_list = arcade.SpriteList()
        self.wall_list = arcade.SpriteList()

        # Score
        self.score = 0

        # Set up player
        self.player_sprite = arcade.Sprite("fishPink.png", PLAYER_SCALE, flipped_horizontally=True)
        self.player_sprite.center_x = 50
        self.player_sprite.center_y = 50
        self.player_list.append(self.player_sprite)

        # Create the Coins
        for i in range(COIN_COUNT):
            coin = Coin("coinGold_ul.png", COIN_SCALE)

            coin.center_x = random.randrange(SCREEN_WIDTH)
            coin.center_y = random.randrange(120, SCREEN_HEIGHT)
            coin.change_x = random.randrange(-3, 4)
            coin.change_y = random.randrange(-3, 4)

        # Place Walls
        wall = arcade.Sprite("button_square_blue_pressed.png", SPRITE_SCALING_BOX)
        wall.center_x = 300
        wall.center_y = 200
        self.wall_list.append(wall)

        wall = arcade.Sprite("button_square_blue_pressed.png", SPRITE_SCALING_BOX)
        wall.center_x = 364
        wall.center_y = 200
        self.wall_list.append(wall)

        for i in range(10):
            wall = arcade.Sprite("button_square_blue_pressed.png", SPRITE_SCALING_BOX)
            wall.center_x = i * 64 + 128
            wall.center_y = 400
            self.wall_list.append(wall)

        for x in range(100, 600, 64):
            wall = arcade.Sprite("button_square_blue_pressed.png", SPRITE_SCALING_BOX)
            wall.center_x = x
            wall.center_y = 100
            self.wall_list.append(wall)

        coordinate_list = [[400, 500],
                           [470, 500],
                           [400, 570],
                           [470, 570]]
        coordinate_list = [[220, 425],
                           [280, 445],
                           [495, 445],
                           [440, 444]]


        for coordinate in coordinate_list:
            wall = arcade.Sprite("button_square_blue_pressed.png", SPRITE_SCALING_BOX)
            wall.center_x = coordinate[0]
            wall.center_y = coordinate[1]
            self.wall_list.append(wall)

        self.physics_engine = arcade.PhysicsEngineSimple(self.player_sprite, self.wall_list)

    def on_draw(self):
        arcade.start_render()

        self.camera_for_sprites.use()

        self.player_list.draw()
        self.wall_list.draw()

        self.camera_for_gui.use()
        arcade.draw_text(f"Score: {self.score}", 10, 10, arcade.color.WHITE, 24)

    def update(self, delta_time):
        self.player_sprite.update()
        self.physics_engine.update()
        if len(self.coin_list) != 0:
            self.coin_list.update()
        CAMERA_SPEED = 1
        lower_left_corner = (self.player_sprite.center_x - self.width / 2,
                             self.player_sprite.center_y - self.height / 2)
        self.camera_for_sprites.move_to(lower_left_corner, CAMERA_SPEED)

    def on_key_press(self, key, modifiers):
        """Called whenever a key is pressed. """

        if key == arcade.key.UP:
            self.player_sprite.change_y = MOVEMENT_SPEED
        elif key == arcade.key.DOWN:
            self.player_sprite.change_y = -MOVEMENT_SPEED
        elif key == arcade.key.LEFT:
            self.player_sprite.change_x = -MOVEMENT_SPEED
        elif key == arcade.key.RIGHT:
            self.player_sprite.change_x = MOVEMENT_SPEED

    def on_key_release(self, key, modifiers):
        """Called when the user releases a key. """

        if key == arcade.key.UP or key == arcade.key.DOWN:
            self.player_sprite.change_y = 0
        elif key == arcade.key.LEFT or key == arcade.key.RIGHT:
            self.player_sprite.change_x = 0


def main():
    """ Main method """
    window = MyGame()
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()

