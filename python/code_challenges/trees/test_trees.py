from binary_tree import BinaryTree, BinarySearchTree
from tree_breadth_first import breadth_first
from node import Node

import pytest

def test_empty_tree():
    bt = BinaryTree()
    assert bt.root == None
    assert bt.root != 1

def test_tree_with_root():
    bt = BinaryTree(1)
    assert bt.root.value == 1
    assert bt.root.value != None

def test_add():
    bt = BinaryTree()
    bts = BinarySearchTree(bt)
    #add to empty
    bts.add(5)
    assert bt.root.value == 5
    assert bt.root.left == None
    assert bt.root.right == None
    #add to left
    bts.add(3)
    assert bt.root.left.value == 3
    assert bt.root.right == None
    #add to left again
    bts.add(1)
    assert bt.root.right == None
    assert bt.root.left.left.value == 1
    #add to right from the top
    bts.add(8)
    assert bt.root.right.value == 8
    #add to right again
    bts.add(10)
    assert bt.root.right.right.value == 10

def test_pre_order(sample_tree):
    assert sample_tree.pre_order() == ["A", "B", "D", "E", "C", "F"]
    assert sample_tree.pre_order() != sample_tree.in_order()
    assert sample_tree.pre_order() != sample_tree.post_order()

def test_in_order(sample_tree):
    assert sample_tree.in_order() == ["D", "B", "E", "A", "F", "C"]
    assert sample_tree.in_order() != sample_tree.pre_order()
    assert sample_tree.in_order() != sample_tree.post_order()

def test_post_order(sample_tree):
    assert sample_tree.post_order() == ["D", "E", "B", "F", "C", "A"]
    assert sample_tree.post_order() != sample_tree.pre_order()
    assert sample_tree.post_order() != sample_tree.in_order()

def test_empty_traversal():
    bt = BinaryTree()
    with pytest.raises(Exception) as pre_order_empty:
        bt.pre_order()
    assert str(pre_order_empty.value) == "The tree is empty!"
    with pytest.raises(Exception) as in_order_empty:
        bt.in_order()
    assert str(in_order_empty.value) == "The tree is empty!"
    with pytest.raises(Exception) as post_order_empty:
        bt.post_order()
    assert str(post_order_empty.value) == "The tree is empty!"

def test_contains_method():
    bt = BinaryTree(1)
    bts = BinarySearchTree(bt)
    bts.add(2)
    bts.add(3)
    bts.add(4)
    bts.add(5)
    bts.add(6)
    bts.add(7)
    assert bts.contains(5) == True
    assert bts.contains(10) == False

def test_find_max_sample():
    bt = BinaryTree(2)
    bt.root.left = Node(3)
    bt.root.left.left = Node(7)
    bt.root.left.right = Node(5)
    bt.root.right = Node(4)
    bt.root.right.left = Node(1)
    bt.root.right.right = Node(9)

    assert bt.tree_max() == 9
    assert bt.tree_max() != 2

def test_find_max_unilateral_right():
    bt = BinaryTree(1)
    bts = BinarySearchTree(bt)
    bts.add(2)
    bts.add(3)
    bts.add(4)
    bts.add(5)
    bts.add(6)
    bts.add(7)
    assert bt.tree_max() == 7
    assert bt.tree_max() != 1

def test_find_max_unilateral_left():
    bt = BinaryTree(7)
    bts = BinarySearchTree(bt)
    bts.add(6)
    bts.add(5)
    bts.add(4)
    bts.add(3)
    bts.add(2)
    bts.add(1)
    assert bt.tree_max() == 7
    assert bt.tree_max() != 1

def test_find_max_empty_tree():
    bt = BinaryTree()
    with pytest.raises(Exception) as max_empty:
        bt.tree_max()
    assert str(max_empty.value) == "The tree is empty!"

def test_breadth_first(sample_tree):
    assert breadth_first(sample_tree) == ["A", "B", "C", "D", "E", "F"]
    assert breadth_first(sample_tree) != ["A", "B", "D", "E", "C", "F"]
    assert breadth_first(sample_tree) != ["D", "B", "E", "A", "F", "C"]
    assert breadth_first(sample_tree) != ["D", "E", "B", "F", "C", "A"]

def test_breadth_first_empty():
    bt = BinaryTree()
    with pytest.raises(Exception) as breadth_first_empty:
        breadth_first(bt)
    assert str(breadth_first_empty.value) == "The tree is empty!"

@pytest.fixture
def sample_tree():
    bt = BinaryTree("A")
    bt.root.left = Node("B")
    bt.root.left.left = Node("D")
    bt.root.left.right = Node("E")
    bt.root.right = Node("C")
    bt.root.right.left = Node("F")

    return bt
