# Trees
* New implementation for trees

## Challenge
* Create a new implementation that includes a Node, Binary Tree, and Binary Search Tree class. 

## Approach & Efficiency
* I used the reading as a supplement on this challenge. The add and contain method shared similar logic.

## API
N/A

# Tree Max
Write a method that finds the maximum value in a binary tree

## Whiteboard Process
![Tree Max Whiteboard](https://github.com/minxie97/data-structures-and-algorithms/blob/tree-max/python/code_challenges/trees/tree_max.jpg)

## Approach & Efficiency
The approach was to use recursion to traverse down both sides of the tree to ultimately find the biggest value on each side. Once it reaches back up to the top, we compare which value is bigger and return that value
Time complexity is O(N^2) and that depends on how deep the tree goes. Space is O(1).

## Solution
* [code](https://github.com/minxie97/data-structures-and-algorithms/blob/tree-max/python/code_challenges/trees/binary_tree.py)
* [tests](https://github.com/minxie97/data-structures-and-algorithms/blob/tree-max/python/code_challenges/trees/test_trees.py)

# Tre Breadth First
Write a function that returns all the values in the tree with in the order that they are encountered in

## Whiteboard Process
![Tree Max Whiteboard](https://github.com/minxie97/data-structures-and-algorithms/blob/tree-breadth-first/python/code_challenges/trees/tree_breadth_first.jpg)

## Approach & Efficiency
The approach was to utilize two lists, where one is a "queue" and the other is the results. As we traverse we "enqueue" nodes into the queue list while "dequeuing" the first up. Whatever we dequeue we append to the results.
Big O is O(N) for both time and space. Time is dependent on how many nodes are on the tree, as well as space. 

## Solution
* [code](https://github.com/minxie97/data-structures-and-algorithms/blob/tree-breadth-first/python/code_challenges/trees/binary_tree.py)
* [tests](https://github.com/minxie97/data-structures-and-algorithms/blob/tree-breadth-first/python/code_challenges/trees/test_trees.py)
