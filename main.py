import numpy as np
import matplotlib.pyplot as plt

# define point


class Point(object):

    def __init__(self):
        self.adjacents = []
        self.movable = True

    def setPosition(self, x, y):  # makes vertex immovable and pins it to given points
        self.x = x
        self.y = y
        self.movable = False

    def addEdge(self, adjacentVert):  # add a vertex to adjacency list
        self.adjacents.append(adjacentVert)

    def getAdjacents(self):
        return self.adjacents


class Graph(object):

    def __init__(self, numVert):  # create list of all verteces
        self.verteces = []
        self.numVert = numVert
        for i in range(numVert):
            self.verteces.append(Point())
            if(i == 0):
                self.verteces[0].setPosition(1, 1)

    # populates list of all adjacent verteces to specified vertex

    def connectEdge(self, vertNum, adjacentVerts):
        for i in range(len(adjacentVerts)):
            # adds edge to selected vertex
            self.verteces[vertNum].addEdge(adjacentVerts[i])

    def printGraphToConsole(self):
        for i in range(self.numVert):

            vertList = self.verteces[i].getAdjacents()
            print("{" + str(i) + "}->" + str(vertList))


# (A,B),(B,C),(C,A)
mainGraph = Graph(3)
mainGraph.connectEdge(0, [1, 2])
mainGraph.connectEdge(1, [0, 2])
mainGraph.connectEdge(2, [0, 1])
mainGraph.printGraphToConsole()

# pts = []
# pts.append(Point([]))
# pts[0].setPosition(1, 2)
# pts.append([Point(pts[0])])

# plt.plot([pts[0].adjacents[0], pts[1].adjacents[1]],
#          [pts[0].adjacents[0], pts[1].adjacents[1]], 'ro-')


# plt.show()
