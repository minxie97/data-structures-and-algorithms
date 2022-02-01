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