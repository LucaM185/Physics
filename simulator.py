import cv2
import numpy as np


size = (640, 480)

class atom:
    def __init__(self):
        self.pos = np.random.rand((2))*np.array(size)
        self.spd = np.random.rand((2))*np.array(size)
        self.radius = np.random.rand()*5 + 4
        

class world: 
    def __init__(self):
        self.atoms = [atom() for i in range(80)]
        self.timestep = 0.003

    def draw(self):
        m = np.zeros((size[1], size[0], 3), dtype=np.uint8)
        for atom in self.atoms:
            cv2.circle(m, np.uint16(atom.pos), np.uint16(atom.radius), (255, 255, 255), -1)

        return m
    
    def collision(self, a, b):
        if np.linalg.norm(a.pos - b.pos) < a.radius + b.radius:
            a.spd, b.spd = b.spd, a.spd
            a.pos += a.spd*self.timestep*2
            b.pos += b.spd*self.timestep*2

    def step(self):
        for atom in self.atoms:
            atom.pos += atom.spd*self.timestep
            for other in self.atoms:
                if atom != other:
                    self.collision(atom, other) 
            if atom.pos[0] < 0 or atom.pos[0] > size[0]:
                atom.spd[0] *= -1
            if atom.pos[1] < 0 or atom.pos[1] > size[1]:
                atom.spd[1] *= -1


w = world()


for i in range(10000):
    w.step()
    cv2.imshow('image', w.draw())
    k = cv2.waitKey(1)
    if k == 27 or k == ord('q'):
        break

cv2.destroyAllWindows()