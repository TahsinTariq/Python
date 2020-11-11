from p5 import *

def setup():
    size(600,600)
    background(0)

def draw():
    begin_shape()
    fill(255, 0,0)
    vertex(100,100)
    fill( 0,255, 0)
    vertex(400,100)
    fill(0,0, 255)
    vertex(100,500)
    end_shape()

run(mode='P3D')