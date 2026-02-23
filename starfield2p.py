from py5 import *
from starfieldp import Star
import py5 
def settings():
    size(800, 800)
stars = []
def setup():

    for i in range(800):
        stars.append(Star())
        



def draw():

    speed = py5.remap(py5.mouse_x, 0, py5.width, 0, 50)
    #speed = 20
    background(0)
    translate(py5.width/2, py5.height/2)

    for s in stars:
        s.update(speed)
        s.show()

run_sketch()