from py5 import *
import random
import py5

class Star:
    def __init__(self):
        self.x = random.uniform(-py5.width, py5.width)
        self.y = random.uniform(-py5.height, py5.height)
        self.z = random.uniform(-py5.width, py5.width)
        self.pz = self.z

    def update(self, speed):
        self.z -= speed
        if self.z < 1:
            self.z = py5.width
            self.x = random.uniform(-py5.width, py5.width)
            self.y = random.uniform(-py5.height, py5.height)
            self.pz = self.z

    def show(self):
        fill(255)
        no_stroke()

        sx = py5.remap(self.x / self.z, -1, 1, 0, py5.width)
        sy = py5.remap(self.y / self.z, -1, 1, 0, py5.height)
        r = py5.remap(self.z, 0, py5.width, 10, 0)

        ellipse(sx, sy, r, r)

        px = py5.remap(self.x / self.pz, -1, 1, 0, py5.width)
        py = py5.remap(self.y / self.pz, -1, 1, 0, py5.height)
        self.pz = self.z

        stroke(255)
        line(px, py, sx, sy)
