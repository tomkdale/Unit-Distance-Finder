import numpy as np
import matplotlib.pyplot as plt
import random as rand


class Point(object):
    '''
    Defines Point to be used by Graph
    '''

    def __init__(self):
        self.adjacents = []
        self.x = 0
        self.y = 0
        self.movable = True
        self.counter = 0

    @property
    def position(self):  # makes vertex immovable and pins it to given points
        return self.x, self.y

    @position.setter
    def position(self, pos):
        if len(pos) is not 2:
            raise ValueError('Can only accept 2-dimensional positions')
        self.movable = False
        self.x, self.y = pos

    def addEdge(self, adjacentVert):  # add a vertex to adjacency list
        self.adjacents.append(adjacentVert)

    def getAllAdjacents(self):
        return self.adjacents

    def getNextAdjacent(self):
        '''
        returns a new connected vertex or -1 if all verteces have been visited
        '''
        if(self.counter >= len(self.adjacents)):
            return -1
        else:
            nextAdjacent = self.adjacents[self.counter]
            self.counter += 1
            return nextAdjacent


class Graph(object):

    def __init__(self, numVert):  
        '''
        Create list of all verteces
        '''
        self.verteces = []
        self.numVert = numVert
        for i in range(numVert):
            self.verteces.append(Point())

    # populates list of all adjacent verteces to specified vertex

    def connectEdge(self, vertNum, adjacentVerts):
        for i in range(len(adjacentVerts)):
            # adds edge to selected vertex
            self.verteces[vertNum].addEdge(adjacentVerts[i])

    def printGraphToConsole(self):
        for i in range(self.numVert):
            vertList = self.verteces[i].getAllAdjacents()
            print("{" + str(i) + "}->" + str(vertList))

    def setLocations(self):  # not Final
        self.verteces[0].position = (0.1, 0)
        self.verteces[1].position = (4.1, 0)
        self.verteces[2].position = (2.1, 2)

    def randomizeLocations(self):
        for i in range(len(self.verteces)):
            self.verteces[i].position = (
                rand.randrange(10), rand.randrange(10)
            )

    def drawableGraph(self):  # recusive function creates list of values for pyplot
        # returns connections in the form (1x,1y,2x,2y...) where every 4 values represents on edge
        drawable = []
        for i in range(len(self.verteces)):
            other = self.verteces[i].getNextAdjacent()
            while (other != -1):
                drawable.append(self.verteces[i].x)
                drawable.append(self.verteces[i].y)
                drawable.append(self.verteces[other].x)
                drawable.append(self.verteces[other].y)
                other = self.verteces[i].getNextAdjacent()

        return drawable


# (A,B),(B,C),(C,A)
mainGraph = Graph(3)
mainGraph.connectEdge(0, [1, 2])
mainGraph.connectEdge(1, [0])
mainGraph.connectEdge(2, [1])
mainGraph.randomizeLocations()
drawable = mainGraph.drawableGraph()
print(drawable)
mainGraph.printGraphToConsole()

# pts = []
# pts.append(Point([]))
# pts[0].setPosition(1, 2)
# pts.append([Point(pts[0])])

for i in range(0, len(drawable), 4):
    plt.plot([drawable[i], drawable[i+2]],
             [drawable[i+1], drawable[i+3]], 'ro-')


plt.show()
