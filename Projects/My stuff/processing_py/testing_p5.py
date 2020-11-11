# from p5 import *
#
# def setup():
# 	createCanvas(640,480)
#
# def draw():
# 	background(random_uniform(255))

from p5 import *


def setup():
    size(640, 360)
    # no_stroke()
    background(204)


def draw():
    if mouse_is_pressed:
        fill(random_uniform(255), random_uniform(127), random_uniform(51), 127)
    else:
        fill(255, 15)

    circle_size = random_uniform(10, 80)

    circle((mouse_x, mouse_y), circle_size)


def key_pressed(event):
    background(204)


if __name__ == '__main__':
    run()
