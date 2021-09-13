"""
This is Lab 2.
"""

# Import the "arcade" library
import arcade

# Open up a window.
# From the "arcade" library, use a function called "open_window"
# Set the window title to "Drawing Example"
# Set the dimensions (width and height)
arcade.open_window(600, 600, "Lab Two Drawing")

# Set the background color
arcade.set_background_color(arcade.csscolor.CADET_BLUE)

# Get ready to draw
arcade.start_render()

# Drawing Grass
arcade.draw_lrtb_rectangle_filled(0, 599, 300, 0, arcade.csscolor.DARK_GREEN)

# Drawing Sun
arcade.draw_circle_filled(50, 550, 40, arcade.color.YELLOW_ORANGE)

# Drawing a Silo
arcade.draw_rectangle_filled(400, 400, 100, 200, arcade.color.GRAY)
arcade.draw_arc_filled(400, 500, 100, 150, arcade.csscolor.BROWN, 0, 180)
arcade.draw_line(400, 300, 400, 500, arcade.color.BLACK)
arcade.draw_line(350, 300, 350, 500, arcade.color.BLACK)
arcade.draw_line(450, 300, 450, 500, arcade.color.BLACK)

# Drawing Silo Lines
arcade.draw_line(350, 300, 450, 300, arcade.color.BLACK)
arcade.draw_line(350, 320, 450, 320, arcade.color.BLACK)
arcade.draw_line(350, 340, 450, 340, arcade.color.BLACK)
arcade.draw_line(350, 360, 450, 360, arcade.color.BLACK)
arcade.draw_line(350, 380, 450, 380, arcade.color.BLACK)
arcade.draw_line(350, 400, 450, 400, arcade.color.BLACK)
arcade.draw_line(350, 420, 450, 420, arcade.color.BLACK)
arcade.draw_line(350, 440, 450, 440, arcade.color.BLACK)
arcade.draw_line(350, 460, 450, 460, arcade.color.BLACK)
arcade.draw_line(350, 480, 450, 480, arcade.color.BLACK)
arcade.draw_line(350, 500, 450, 500, arcade.color.BLACK)

# Drawing a Tree
arcade.draw_rectangle_filled(200, 350, 20, 100, arcade.csscolor.SIENNA)
arcade.draw_ellipse_filled(200, 400, 60, 80, arcade.csscolor.DARK_GREEN)

# Drawing a Garden
arcade.draw_rectangle_filled(300, 150, 300, 200, (160, 64, 0))

# Draw Vegetables
arcade.draw_circle_filled(180, 200, 20, arcade.color.ORIOLES_ORANGE)
arcade.draw_circle_outline(180, 200, 20, arcade.color.GOLD)
arcade.draw_circle_filled(240, 200, 20, arcade.color.ORIOLES_ORANGE)
arcade.draw_circle_outline(240, 200, 20, arcade.color.GOLD)
arcade.draw_circle_filled(320, 200, 20, arcade.color.ORIOLES_ORANGE)
arcade.draw_circle_outline(320, 200, 20, arcade.color.GOLD)
arcade.draw_circle_filled(420, 200, 20, arcade.color.ORIOLES_ORANGE)
arcade.draw_circle_outline(420, 200, 20, arcade.color.GOLD)

# Draw Fruit in Red
arcade.draw_ellipse_filled(270, 90, 20, 20, arcade.color.ALIZARIN_CRIMSON)
arcade.draw_ellipse_filled(300, 90, 20, 20, arcade.color.ALIZARIN_CRIMSON)
arcade.draw_ellipse_filled(250, 90, 20, 20, arcade.color.ALIZARIN_CRIMSON)
arcade.draw_ellipse_filled(420, 90, 20, 20, arcade.color.ALIZARIN_CRIMSON)
arcade.draw_ellipse_filled(200, 90, 20, 20, arcade.color.ALIZARIN_CRIMSON)
arcade.draw_ellipse_filled(180, 90, 20, 20, arcade.color.ALIZARIN_CRIMSON)
arcade.draw_ellipse_filled(320, 90, 20, 20, arcade.color.ALIZARIN_CRIMSON)
arcade.draw_ellipse_filled(400, 90, 20, 20, arcade.color.ALIZARIN_CRIMSON)

# Draw Text at (160, 130) with a font size of 20 pts.
arcade.draw_text("Live Life to the Fullest!",
                 160, 130,
                 arcade.color.BLACK, 20)

# Finish drawing
arcade.finish_render()

# Keep the window up until someone closes it.
arcade.run()
