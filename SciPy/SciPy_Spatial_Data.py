import numpy as np
import matplotlib.pyplot as plt

#A Triangulation of a polygon is to divide the polygon into multiple triangles with which we can compute an area of the polygon.
from scipy.spatial import Delaunay

points = np.array([
  [2, 4],
  [3, 4],
  [3, 0],
  [2, 2],
  [4, 1]
])

simplices = Delaunay(points).simplices
#The simplices property creates a generalization of the triangle notation.
plt.triplot(points[:, 0], points[:, 1], simplices)
plt.scatter(points[:, 0], points[:, 1], color='r')

plt.show()

#A convex hull is the smallest polygon that covers all of the given points.
from scipy.spatial import ConvexHull

points = np.array([
  [2, 4], [3, 4], [3, 0],
  [2, 2],
  [4, 1], [1, 2], [5, 0],
  [3, 1], [1, 2], [0, 2]
])

hull = ConvexHull(points)
hull_points = hull.simplices

plt.scatter(points[:,0], points[:,1])
for simplex in hull_points:
    plt.plot(points[simplex,0], points[simplex,1], 'k-')

plt.show()

#KDTrees are a datastructure optimized for nearest neighbor queries.
from scipy.spatial import KDTree

points = [(1, -1), (2, 3), (-2, 3), (2, -3)]

kdtree = KDTree(points) #KDTree() method returns a KDTree object.
res = kdtree.query((1, 1))  #query() method returns the distance to the nearest neighbor and the location of the neighbors.
print(res)


#Find the euclidean distance between given points.
from scipy.spatial.distance import euclidean

p1 = (1, 0)
p2 = (10, 2)

res = euclidean(p1, p2)
print(res)

#Cityblock Distance (Manhattan Distance) : Is the distance computed using 4 degrees of movement.
#E.g. we can only move: up, down, right, or left, not diagonally.
from scipy.spatial.distance import cityblock

p1 = (1, 0)
p2 = (10, 2)

res = cityblock(p1, p2)
print(res)


#Cosine Distance : Is the value of cosine angle between the two points A and B.
from scipy.spatial.distance import cosine

p1 = (1, 0)
p2 = (10, 2)

res = cosine(p1, p2)
print(res)

#Hamming Distance : Is the proportion of bits where two bits are difference.
#It's a way to measure distance for binary sequences.
from scipy.spatial.distance import hamming

p1 = (True, False, True)
p2 = (False, True, True)

res = hamming(p1, p2)
print(res)








