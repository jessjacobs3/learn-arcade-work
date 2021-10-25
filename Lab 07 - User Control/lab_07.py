""" Lab 7 - User Control """

import arcade

# --- Constants ---
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
MOVEMENT_SPEED = 10


class Volleyball:
    def __init__(self, position_x, position_y, change_x, change_y, radius, color):
        # Take the parameters of the init function above,
        # and create instance variables out of them.
        self.position_x = position_x
        self.position_y = position_y
        self.change_x = change_x
        self.change_y = change_y
        self.radius = radius
        self.color = color

    def draw(self):
        """ Draw the balls with the instance variables we have. """
        arcade.draw_circle_filled(self.position_x,
                                  self.position_y,
                                  self.radius,
                                  self.color)
        arcade.draw_circle_filled(self.position_x, self.position_y + 10, self.radius, self.color)
        arcade.draw_circle_filled(self.position_x, self.position_y + 13, self.radius, self.color)
        arcade.draw_circle_filled(self.position_x, self.position_y + 15, self.radius, self.color)
        arcade.draw_circle_filled(self.position_x, self.position_y + 20, self.radius, self.color)

    def update(self):
        # Move the ball
        self.position_y += self.change_y
        self.position_x += self.change_x

        if self.position_x < self.radius:
            self.position_x = self.radius

        if self.position_x > SCREEN_WIDTH - self.radius:
            self.position_x = SCREEN_WIDTH - self.radius

        if self.position_y < self.radius:
            self.position_y = self.radius

        if self.position_y > SCREEN_HEIGHT - self.radius:
            self.position_y = SCREEN_HEIGHT - self.radius


class Basketball:
    def __init__(self, position_x, position_y, change_x, change_y, radius, color):
        # Take the parameters of the init function above,
        # and create instance variables out of them.
        self.position_x = position_x
        self.position_y = position_y
        self.change_x = change_x
        self.change_y = change_y
        self.radius = radius
        self.color = color
        self.sound_two = arcade.load_sound(":resources:sounds/upgrade4.wav")

    def draw(self):
        """ Draw the balls with the instance variables we have. """
        arcade.draw_circle_filled(self.position_x,
                                  self.position_y,
                                  self.radius,
                                  self.color)
        arcade.draw_circle_filled(self.position_x, self.position_y - 7, self.radius, self.color)
        arcade.draw_circle_filled(self.position_x, self.position_y - 8, self.radius, self.color)
        arcade.draw_circle_filled(self.position_x, self.position_y - 9, self.radius, self.color)
        arcade.draw_circle_filled(self.position_x, self.position_y - 10, self.radius, self.color)

    def update(self):
        # Move the ball
        self.position_y += self.change_y
        self.position_x += self.change_x

        if self.position_x < self.radius:
            self.position_x = self.radius
            arcade.play_sound(self.sound_two)

        if self.position_x > SCREEN_WIDTH - self.radius:
            self.position_x = SCREEN_WIDTH - self.radius
            arcade.play_sound(self.sound_two)

        if self.position_y < self.radius:
            self.position_y = self.radius
            arcade.play_sound(self.sound_two)

        if self.position_y > SCREEN_HEIGHT - self.radius:
            self.position_y = SCREEN_HEIGHT - self.radius
            arcade.play_sound(self.sound_two)


class MyGame(arcade.Window):
    def __init__(self):
        # Call the parent class's init function
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "Lab 7")

        self.set_mouse_visible(False)

        arcade.set_background_color(arcade.color.REDWOOD)

        # Create our ball
        self.ball = Volleyball(10, 10, 0, 0, 15, arcade.color.BUFF)
        self.basketball = Basketball(10, 10, 0, 0, 15, arcade.color.SKY_BLUE)

        self.sound_one = arcade.load_sound(":resources:sounds/jump3.wav")

    def on_draw(self):
        """ Called whenever we need to draw the window. """
        arcade.start_render()
        arcade.draw_lrtb_rectangle_filled(0, 599, 300, 0, arcade.csscolor.DARK_GREEN)
        arcade.draw_rectangle_filled(200, 350, 20, 100, arcade.csscolor.SIENNA)
        arcade.draw_ellipse_filled(200, 400, 60, 80, arcade.csscolor.DARK_GREEN)
        self.ball.draw()
        self.basketball.draw()

    def on_mouse_motion(self, x, y, dx, dy):
        self.ball.position_x = x
        self.ball.position_y = y

    def on_mouse_press(self, x, y, button, modifiers):
        """ Called when the user presses a mouse button. """
        if button == arcade.MOUSE_BUTTON_LEFT:
            arcade.play_sound(self.sound_one)
        elif button == arcade.MOUSE_BUTTON_RIGHT:
            arcade.play_sound(self.sound_one)

    def update(self, delta_time: float):
        self.ball.update()
        self.basketball.update()

    def on_key_press(self, key, modifiers):
        """ Called whenever the user presses a key. """
        if key == arcade.key.LEFT:
            self.basketball.change_x = -MOVEMENT_SPEED

        elif key == arcade.key.RIGHT:
            self.basketball.change_x = MOVEMENT_SPEED

        elif key == arcade.key.UP:
            self.basketball.change_y = MOVEMENT_SPEED

        elif key == arcade.key.DOWN:
            self.basketball.change_y = -MOVEMENT_SPEED

    def on_key_release(self, key, modifiers):
        """ Called whenever a user releases a key. """
        if key == arcade.key.LEFT or key == arcade.key.RIGHT:
            self.basketball.change_x = 0
        elif key == arcade.key.UP or key == arcade.key.DOWN:
            self.basketball.change_y = 0


def main():
    window = MyGame()
    arcade.run()


main()
