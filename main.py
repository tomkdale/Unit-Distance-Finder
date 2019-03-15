import numpy as np
import matplotlib.pyplot as plt

# define point


class Point(object):
    # var x,y
    def __init__(self, connections):
        self.x = connections[0]
        self.y = connections[1]


numPts = 3

pts = []
for i in range(numPts):
    pts.append(Point([i, i+2]))


plt.plot([pts[0].x, pts[1].x], [pts[0].y, pts[1].y], 'ro-')


plt.show()
