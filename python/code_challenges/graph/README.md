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