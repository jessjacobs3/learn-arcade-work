import arcade

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600


def draw_sky():
    """Draw the Sky"""
    # Draw the ground
    arcade.draw_lrtb_rectangle_filled(0, SCREEN_WIDTH, SCREEN_HEIGHT / 2, 0, arcade.color.SKY_BLUE)

def draw_snow_man(x, y):
    """Draw A Snow Man"""

    # Draw Snow
    arcade.draw_circle_filled(x + 400, 300 + y, 40, arcade.color.WHITE)
    arcade.draw_circle_filled(x + 400, 350 + y, 35, arcade.color.WHITE)
    arcade.draw_circle_filled(x + 400, 400 + y, 30, arcade.color.WHITE)

    # Draw Eyes
    arcade.draw_circle_filled(x + 385, y + 410, 5, arcade.color.BLACK, num_segments=32)
    arcade.draw_circle_filled(x + 415, y + 410, 5, arcade.color.BLACK, num_segments=32)

def draw_little_snowball(x, y):
    """Draw a Little Snowball"""
    arcade.draw_circle_filled(x + 200, y + 200, 5, arcade.color.WHITE, num_segments=32)

def draw_big_snowball(x, y):
    """Draw a Big Snowball"""
    arcade.draw_circle_filled(x + 300, y + 420, 10, arcade.color.FLORAL_WHITE, num_segments=32)

def draw_snowflake(x, y):
    """Draw a Snowflake"""
    arcade.draw_line(x, y, x + 10, y + 20, arcade.color.WHITE)
    arcade.draw_line(x, y + 15, x + 10, y - 10, arcade.color.WHITE)
    arcade.draw_line(x, y + 5, x + 10, y + 5, arcade.color.WHITE)

def main():
    arcade.open_window(SCREEN_WIDTH, SCREEN_HEIGHT, "Drawing with Functions")
    arcade.set_background_color(arcade.color.BLUE_YONDER)
    arcade.start_render()

    draw_sky()
    draw_big_snowball(200, 45)
    draw_big_snowball(150, 50)
    draw_big_snowball(100, 25)
    draw_big_snowball(200, 55)
    draw_big_snowball(100, 20)
    draw_big_snowball(10, 10)
    draw_big_snowball(50, 50)
    draw_big_snowball(90, 90)
    draw_big_snowball(25, 25)
    draw_snow_man(150, 40)
    draw_snow_man(15, 40)
    draw_snow_man(-200, -10)
    draw_snow_man(-100, -40)
    draw_little_snowball(200, 100)
    draw_little_snowball(10, 10)
    draw_little_snowball(-10, -10)
    draw_little_snowball(-20, -20)
    draw_little_snowball(-25, -25)
    draw_little_snowball(-10, -10)
    draw_snowflake(250, 500)
    draw_snowflake(210, 200)
    draw_snowflake(430, 500)
    draw_snowflake(100, 500)
    draw_snowflake(75, 400)
    draw_snowflake(340, 125)
    draw_snowflake(80, 170)
    draw_snowflake(490, 520)
    draw_snowflake(360, 140)
    draw_snowflake(380, 175)

    arcade.finish_render()
    arcade.run()

main()
