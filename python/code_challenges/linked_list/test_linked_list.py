from linked_list import Node, LinkedList
import pytest

def test_node_instance():
    node = Node(1, None)
    assert node.next == None
    assert node.value == 1

def test_node_instance_fail():
    node = Node(1, None)
    assert node.next != node
    assert node.value != 2

def test_linked_list():
    node = Node(1, None)
    ll = LinkedList(node)
    assert ll.head == node

def test_linked_list_empty():
    ll = LinkedList()
    assert ll.head == None

def test_insert_to_empty_linked_list():
    # ll.head = apple
    ll = LinkedList()
    ll.insert('apple')
    assert ll.head.value == 'apple'

def test_head_pointing_to_first_node():
    ll = LinkedList()
    head_node = Node('head')
    ll.head = head_node
    first_node = Node('first')
    ll.head.next = first_node
    assert ll.head.next.value == 'first'

def test_insert_multiple_nodes():
    ll = LinkedList()
    ll.insert('A')
    assert ll.head.value == 'A'
    ll.insert('B')
    assert ll.head.value == 'B'
    assert ll.head.next.value == 'A'
    ll.insert('C')
    assert ll.head.value == 'C'
    assert ll.head.next.value == 'B'
    
def test_finding_value_true():
    ll = LinkedList()
    ll.insert(1)
    ll.insert(2)
    ll.insert(3)
    ll.insert(4)
    ll.insert(5)
    assert ll.includes(3)

def test_finding_value_false():
    ll = LinkedList()
    ll.insert(1)
    ll.insert(2)
    assert ll.includes(1)
    assert ll.includes(3) == False

def test_returning_string():
    ll = LinkedList()
    ll.insert(1)
    ll.insert(2)
    ll.insert(3)
    ll.insert(4)
    ll.insert(5)
    assert ll.to_string() == "5 -> 4 -> 3 -> 2 -> 1 -> NULL"