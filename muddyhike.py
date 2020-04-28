# deque is a double ended queue
#
from collections import deque, namedtuple    
import sys
# first two inputs r = rows and c = columns
# cannot travel diagonally
n = input().split()
row, col = n[0], n[1]
something = []

for id, x in enumerate(sys.stdin):
    x = x.split()
    something.append(x)
    
    if id == row-1:
        break

class dijkstra():
    # Defining all the unvisted nodes as infinity
    inf = float("inf")
    Edge = namedtuple('edges', 'start, end, cost')

    
    # initialising the node.
    # def __init__(self, data, indexloc = 0):
    #     self.data = something
    #     self.indexloc = indexloc

    # def search_neighbor(self,X,Y):
    #     neighbor = []
    #     if 0 < X < row or 0 < Y < col:
    #         up = X