from tree_intersection.tree_intersection import tree_intersection
from trees.binary_tree import BinaryTree
from trees.node import Node
import pytest

def test_tree_intersection(first_tree, second_tree):
    answers = tree_intersection(first_tree, second_tree)
    assert answers == ["D", "A", "F"]

def test_tree_intersection_numbers(int_tree_one, int_tree_two):
    answers = tree_intersection(int_tree_one, int_tree_two)
    assert answers == [2, 5, 10, 7]

def test_no_matches(first_tree, int_tree_one):
    answers = tree_intersection(first_tree, int_tree_one)
    assert answers == []

def test_empty_trees():
    tree1 = BinaryTree()
    tree2 = BinaryTree()
    answers = tree_intersection(tree1, tree2)
    assert answers == []

@pytest.fixture
def first_tree():
    bt = BinaryTree("A")
    bt.root.left = Node("B")
    bt.root.left.left = Node("D")
    bt.root.left.right = Node("E")
    bt.root.right = Node("C")
    bt.root.right.left = Node("F")

    return bt

@pytest.fixture
def second_tree():
    bt = BinaryTree("G")
    bt.root.left = Node("D")
    bt.root.left.left = Node("L")
    bt.root.left.right = Node("A")
    bt.root.right = Node("F")
    bt.root.right.left = Node("X")

    return bt

@pytest.fixture
def int_tree_one():
    bt = BinaryTree(5)
    bt.root.left = Node(2)
    bt.root.left.left = Node(10)
    bt.root.left.right = Node(18)
    bt.root.right = Node(7)
    bt.root.right.left = Node(9)
    bt.root.right.right = Node(1)

    return bt

@pytest.fixture
def int_tree_two():
    bt = BinaryTree(6)
    bt.root.left = Node(5)
    bt.root.left.left = Node(2)
    bt.root.left.right = Node(10)
    bt.root.right = Node(4)
    bt.root.right.left = Node(8)
    bt.root.right.right = Node(7)

    return bt