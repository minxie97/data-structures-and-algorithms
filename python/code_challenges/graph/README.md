# Graphs
Implement Graph

## Challenge
The graph should be represented as an adjacency list, and should include the following methods:
* add_node
* add_edge
* get_nodes
* get_neighbors
* size

## Approach & Efficiency
My approach was really to understand the concept of graphs given to us from the reading and create an implementation with that knowledge plus the clues from the demo.

## API
* add_node
  * Arguments: value
  * Returns: The added node
  * Add a node to the graph
* add_edge
  * Arguments: 2 nodes to be connected by the edge, weight (optional)
  * Returns: nothing
  * Adds a new edge between two nodes in the graph
  * If specified, assign a weight to the edge
  * Both nodes should already be in the Graph
* get_nodes
  * Arguments: none
  * Returns all of the nodes in the graph as a collection (set, list, or similar)
* get_neighbors
  * Arguments: node
  * Returns a collection of edges connected to the given node
  * Include the weight of the connection in the returned collection
* size
  * Arguments: none
  * Returns the total number of nodes in the graph

# Graph Breadth First
write a method that takes a Node as an argument and returns a collection of nodes in the order that they were visited.

## Whiteboard Process
![breadth-first](https://github.com/minxie97/data-structures-and-algorithms/blob/graph-breadth-first/python/code_challenges/graph/graph_breadth_first.jpg)

## Approach & Efficiency
My approach was to utilize a set and queue to figure out which nodes I have visited in the traversal and the order of that traversal. Everytime I reach a node that I have not visited before, I would add it to the set and then enqeue it in the queue. I then add what is deqeued to the return list, ensuring the order. Then I check the dequeued node for its neighbors and check the set if those neighbors have been visited and if not add to the set and enqueue it. Repeat until I go through the whole list.

## Solution
```
def breadth_first(self, node=None):
    nodes = []
    queue = []
    visited = set()

    queue.append(node)
    visited.add(node)

    while len(queue) > 0:
        front = queue.pop(0)
        nodes.append(front.value)

        for i in self.get_neighbor(front):
            if i.vertex not in visited:
                visited.add(i.vertex)
                queue.append(i.vertex)

    return nodes
```
[tests](https://github.com/minxie97/data-structures-and-algorithms/blob/graph-breadth-first/python/code_challenges/graph/test_graphy.py)

# Graph Business Trip
Write a function called business_trip that takes in a graph and array of city names. Determine whether the trip is possible between those cities with direct flights, and how much it would cost.

Return cost if the trip is possible, None if not.

## Whiteboard Process
![business-trip](https://github.com/minxie97/data-structures-and-algorithms/blob/graph-business-trip/python/code_challenges/graph/graph_business_trip.jpg)

## Approach & Efficiency
My approach was to essentially loop through the graph to see if a vertex exists for the departure city and if so check if the arrival city is a direct neighbor of that departure node. If so, that means a direct flight is possible and the cost is added to the return variable.

## Solution
```
def business_trip(graph, cities):
    cost = 0
    for i in range(len(cities) - 1):
        for vertex in graph.get_nodes():
            if vertex.value == cities[i]:
                depart_node = vertex
                break
        else:
            return None
        for neighbor in graph.get_neighbor(depart_node):
            if neighbor.vertex.value == cities[i + 1]:
                cost += neighbor.weight
                break
        else:
            return None
    return cost
```
[tests](https://github.com/minxie97/data-structures-and-algorithms/blob/graph-business-trip/python/code_challenges/graph/test_graphy.py)

# Graph Depth First
write a method that takes a Node as an argument and returns a collection of nodes in pre-order depth-first order.

## Whiteboard Process
![depth-first](https://github.com/minxie97/data-structures-and-algorithms/blob/graph-depth-first/python/code_challenges/graph/graph_depth_first.jpg)

## Approach and efficiency
Depth first traversal is very similar to breadth first except for a few tweaks. We use a stack rather than a queue and we reverse the list of childrens so that we are able to add the first child to the stack last (accessed first).

## Solution
```
def depth_first(self, node=None):

    if node is None: return []

    nodes = []
    stack = []
    visited = set()

    stack.append(node)
    visited.add(node)

    while stack:
        top = stack.pop()
        nodes.append(top.value)

        for i in reversed(self.get_neighbor(top)):
            if i.vertex not in visited:
                visited.add(i.vertex)
                stack.append(i.vertex)

    return nodes
```
[tests](https://github.com/minxie97/data-structures-and-algorithms/blob/graph-depth-first/python/code_challenges/graph/test_graphy.py)
