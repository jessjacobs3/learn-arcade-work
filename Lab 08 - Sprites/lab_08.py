import arcade
import random
import math

# --- Constants ---
SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 800
MOVEMENT_SPEED = 5
PLAYER_SCALE = 0.7
COIN_SCALE = 0.35
COIN_COUNT = 30
SUN_SCALE = 0.35
SUN_COUNT = 30
BULLET_SPEED = 30
LASER_SCALE = 1
TARGET_SCALE = 0.03


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


class Sun(arcade.Sprite):

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

    def __init__(self):

        # Call the parent class initializer
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "Lab 8 Sprites")

        # Sprite lists
        self.player_list = None
        self.coin_list = None
        self.sun_list = None
        self.bullet_list = None
        self.target_list = None

        # Player Info
        self.player_sprite = None
        self.score = 0

        self.target_sprite = None

        self.gun_sound = arcade.load_sound(":resources:sounds/laser2.wav")
        self.good_hit_sound = arcade.sound.load_sound(":resources:sounds/coin1.wav")
        self.bad_hit_sound = arcade.sound.load_sound(":resources:sounds/error5.wav")

        self.time_taken = 0
        arcade.set_background_color(arcade.color.CADET_BLUE)

        self.set_mouse_visible(False)

    def setup(self):

        # Sprite Lists
        self.player_list = arcade.SpriteList()
        self.coin_list = arcade.SpriteList()
        self.sun_list = arcade.SpriteList()
        self.bullet_list = arcade.SpriteList()
        self.target_list = arcade.SpriteList()

        # Score
        self.score = 0

        # Set up player
        # Character image from api.arcade.academy in Python Arcade Library Resources
        self.player_sprite = arcade.Sprite("fishPink.png", PLAYER_SCALE, flipped_horizontally=True)
        self.player_sprite.center_x = 50
        self.player_sprite.center_y = 50
        self.player_list.append(self.player_sprite)

        # Target image from clipart-library.com in Clipart Library
        self.target_sprite = arcade.Sprite("target.png", TARGET_SCALE)
        self.target_sprite.center_x = 60
        self.target_sprite.center_y = 60
        self.target_list.append(self.target_sprite)

        # Create the Coins
        for i in range(COIN_COUNT):

            # Coin image from api.arcade.academy in Python Arcade Library Resources
            coin = Coin("coinGold_ul.png", COIN_SCALE)

            coin.center_x = random.randrange(SCREEN_WIDTH)
            coin.center_y = random.randrange(120, SCREEN_HEIGHT)
            coin.change_x = random.randrange(-3, 4)
            coin.change_y = random.randrange(-3, 4)

            self.coin_list.append(coin)

        for i in range(SUN_COUNT):

            # Sun image from api.arcade.academy in Python Arcade Library Resources
            sun = Sun("bumper.png", SUN_SCALE)

            sun.center_x = random.randrange(SCREEN_WIDTH)
            sun.center_y = random.randrange(120, SCREEN_HEIGHT)
            sun.change_x = random. randrange(-3, 4)
            sun.change_y = random. randrange(-3, 4)

            self.sun_list.append(sun)

    def on_draw(self):

        arcade.start_render()
        self.player_list.draw()
        self.target_list.draw()
        self.coin_list.draw()
        self.sun_list.draw()
        self.bullet_list.draw()

        output = f"score: {self.score}"
        arcade.draw_text(output, 10, 20, arcade.color.WHITE, 30)

        if len(self.coin_list) == 0:
            arcade.draw_text("Game Over",
                             SCREEN_WIDTH / 2,
                             SCREEN_HEIGHT / 2,
                             arcade.color.WHITE, 80,
                             anchor_x="center")

    def on_mouse_motion(self, x, y, dx, dy):
        if len(self.coin_list) != 0:
            self.target_sprite.center_x = x
            self.target_sprite.center_y = y
        else:
            self.set_mouse_visible(True)

    def on_mouse_press(self, x, y, button, modifiers):
        if len(self.sun_list) != 0:
            # Laser image from api.arcade.academy in Python Arcade Library Resources
            bullet = arcade.Sprite("laserRed01.png", LASER_SCALE)

            start_x = self.player_sprite.center_x
            start_y = self.player_sprite.center_y + 30
            bullet.center_x = start_x
            bullet.center_y = start_y

            destination_x = x
            destination_y = y

            x_diff = destination_x - start_x
            y_diff = destination_y - start_y
            angle = math.atan2(y_diff, x_diff)

            bullet.change_x = math.cos(angle) * BULLET_SPEED
            bullet.change_y = math.sin(angle) * BULLET_SPEED

            self.bullet_list.append(bullet)
            arcade.play_sound(self.gun_sound)

    def update(self, delta_time):
        if len(self.coin_list) != 0:
            self.coin_list.update()
            self.sun_list.update()
            self.bullet_list.update()
            self.player_sprite.update()

            good_hit_list = arcade.check_for_collision_with_list(self.player_sprite, self.coin_list)
            bad_hit_list = arcade.check_for_collision_with_list(self.player_sprite, self.sun_list)

            for coin in good_hit_list:
                coin.remove_from_sprite_lists()
                self.score += 1
                arcade.play_sound(self.good_hit_sound)

            for sun in bad_hit_list:
                sun.remove_from_sprite_lists()
                self.score -= 1
                arcade.play_sound(self.bad_hit_sound)

            for bullet in self.bullet_list:

                good_hit_list = arcade.check_for_collision_with_list(bullet, self.coin_list)
                bad_hit_list = arcade.check_for_collision_with_list(bullet, self.sun_list)

                if len(good_hit_list) > 0:
                    bullet.remove_from_sprite_lists()
                for coin in good_hit_list:
                    coin.remove_from_sprite_lists()
                    self.score += 1
                    arcade.play_sound(self.good_hit_sound)

                if len(bad_hit_list) > 0:
                    bullet.remove_from_sprite_lists()
                for sun in bad_hit_list:
                    sun.remove_from_sprite_lists()
                    self.score -= 1
                    arcade.play_sound(self.bad_hit_sound)

                if bullet.bottom > self.width or\
                        bullet.top < 0 or\
                        bullet.right < 0 or\
                        bullet.left > self.width:
                    bullet.remove_from_sprite_lists()

            if self.player_sprite.top > SCREEN_HEIGHT:
                self.player_sprite.top = SCREEN_HEIGHT
            if self.player_sprite.left < 0:
                self.player_sprite.left = 0
            if self.player_sprite.bottom < 0:
                self.player_sprite.bottom = 0
            if self.player_sprite.right > SCREEN_WIDTH:
                self.player_sprite.right = SCREEN_WIDTH

    def on_key_press(self, key, modifiers):

        if key == arcade.key.A:
            self.player_sprite.change_x = -MOVEMENT_SPEED
        elif key == arcade.key.D:
            self.player_sprite.change_x = MOVEMENT_SPEED
        elif key == arcade.key.W:
            self.player_sprite.change_y = MOVEMENT_SPEED
        elif key == arcade.key.S:
            self.player_sprite.change_y = -MOVEMENT_SPEED

    def on_key_release(self, key, modifiers):
        if key == arcade.key.A or key == arcade.key.D:
            self.player_sprite.change_x = 0
        elif key == arcade.key.W or key == arcade.key.S:
            self.player_sprite.change_y = 0


def main():
    window = MyGame()
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()


coin_placed_successfully = False

        while not coin_placed_successfully:
        coin.center_x = random.randrange(50, SCREEN_WIDTH * 2)
        coin.center_y = random.randrange(-400, 400)

        wall_hit_list = arcade.check_for_collision_with_list(coin, self.wall_list)
        coin_hit_list = arcade.check_for_collision_with_list(coin, self.coin_list)

                if len(wall_hit_list) == 0 and len(coin_hit_list) == 0:
                    # It is!
                    coin_placed_successfully = True
