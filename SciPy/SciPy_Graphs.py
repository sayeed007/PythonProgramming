import numpy as np
from scipy.sparse.csgraph import connected_components
from scipy.sparse import csr_matrix


#Find all of the connected components with the connected_components() method.
arr = np.array([
  [0, 1, 1],
  [1, 0, 0],
  [2, 1, 0]
])

newarr = csr_matrix(arr)
print(newarr)
print(connected_components(newarr))


#Use the dijkstra method to find the shortest path in a graph from one element to another.
from scipy.sparse.csgraph import dijkstra

print(dijkstra(newarr, return_predecessors=True, indices=0))


#Use the floyd_warshall() method to find shortest path between all pairs of elements.
from scipy.sparse.csgraph import floyd_warshall

print(floyd_warshall(newarr, return_predecessors=True))

#The bellman_ford() method can also find the shortest path between all pairs of elements, but this method can handle negative weights as well.
from scipy.sparse.csgraph import bellman_ford

arr = np.array([
  [0, -1, 2],
  [1, 0, 0],
  [2, 0, 0]
])

newarr = csr_matrix(arr)
print(bellman_ford(newarr, return_predecessors=True, indices=0))

#The depth_first_order() method returns a depth first traversal from a node.
from scipy.sparse.csgraph import depth_first_order

arr = np.array([
  [0, 1, 0, 1],
  [1, 1, 1, 1],
  [2, 1, 1, 0],
  [0, 1, 0, 1]
])

newarr = csr_matrix(arr)

print(depth_first_order(newarr, 1))

#The breadth_first_order() method returns a breadth first traversal from a node.
from scipy.sparse.csgraph import breadth_first_order

print(breadth_first_order(newarr, 1))





















