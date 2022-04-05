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


## Approach & Efficiency
My approach was to utilize a set and queue to figure out which nodes I have visited in the traversal and the order of that traversal. Everytime I reach a node that I have not visited before, I would add it to the set and then enqeue it in the queue. I then add what is deqeued to the return list, ensuring the order. Then I check the dequeued node for its neighbors and check the set if those neighbors have been visited and if not add to the set and enqueue it. Repeat until I go through the whole list.

## Solution


