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

def test_append_to_end():
    ll = LinkedList()
    ll.insert(1)
    ll.insert(2)
    ll.insert(3)
    ll.insert(4)
    ll.insert(5)
    ll.append(0)
    assert ll.head.value == 5
    assert ll.to_string() == "5 -> 4 -> 3 -> 2 -> 1 -> 0 -> NULL"

def test_append_to_end_fail():
    ll = LinkedList()
    ll.insert(1)
    ll.insert(2)
    ll.insert(3)
    ll.insert(4)
    ll.insert(5)
    ll.append(0)
    assert ll.head.value != 0
    assert ll.to_string() != "0 -> 5 -> 4 -> 3 -> 2 -> 1 -> NULL"

def test_append_to_empty():
    ll = LinkedList()
    ll.append(1)
    assert ll.head.value == 1
    assert ll.to_string() == "1 -> NULL"

def test_append_to_empty_fail():
    ll = LinkedList()
    ll.append(1)
    assert ll.head.value != None
    assert ll.to_string() != "NULL -> 1"

def test_append_multiple():
    ll = LinkedList()
    ll.append(1)
    ll.append(2)
    ll.append(3)
    ll.append(4)
    ll.append(5)
    assert ll.head.value == 1
    assert ll.to_string() == "1 -> 2 -> 3 -> 4 -> 5 -> NULL"

def test_insert_before_middle():
    ll = LinkedList()
    ll.append(1)
    ll.append(2)
    ll.append(3)
    ll.insert_before(2, 5)
    assert ll.to_string() == "1 -> 5 -> 2 -> 3 -> NULL"

def test_insert_before_middle_fail():
    ll = LinkedList()
    ll.append(1)
    ll.append(2)
    ll.append(3)
    ll.insert_before(2, 5)
    assert ll.to_string() != "1 -> 2 -> 5 -> 3 -> NULL"

def test_insert_before_first():
    ll = LinkedList()
    ll.append(1)
    ll.append(2)
    ll.append(3)
    ll.insert_before(1, 5)
    assert ll.head.value == 5
    assert ll.to_string() == "5 -> 1 -> 2 -> 3 -> NULL"

def test_insert_before_first_fail():
    ll = LinkedList()
    ll.append(1)
    ll.append(2)
    ll.append(3)
    ll.insert_before(1, 5)
    assert ll.head.value != 1

def test_insert_before_no_change():
    ll = LinkedList()
    ll.append(1)
    ll.append(2)
    ll.append(3)
    ll.insert_before(4, 5)
    assert ll.to_string() == "1 -> 2 -> 3 -> NULL"

def test_insert_after_middle():
    ll = LinkedList()
    ll.append(1)
    ll.append(2)
    ll.append(3)
    ll.insert_after(2, 5)
    assert ll.to_string() == "1 -> 2 -> 5 -> 3 -> NULL"

def test_insert_after_middle_fail():
    ll = LinkedList()
    ll.append(1)
    ll.append(2)
    ll.append(3)
    ll.insert_after(2, 5)
    assert ll.to_string() != "1 -> 5 -> 2 -> 3 -> NULL"

def test_insert_after_last():
    ll = LinkedList()
    ll.append(1)
    ll.append(2)
    ll.append(3)
    ll.insert_after(3, 5)
    assert ll.to_string() == "1 -> 2 -> 3 -> 5 -> NULL"

def test_insert_after_last_fail():
    ll = LinkedList()
    ll.append(1)
    ll.append(2)
    ll.append(3)
    ll.insert_after(3, 5)
    assert ll.to_string() != "1 -> 2 -> 5 -> 3 -> NULL"

def test_insert_after_no_change():
    ll = LinkedList()
    ll.append(1)
    ll.append(2)
    ll.append(3)
    ll.insert_after(4, 5)
    assert ll.to_string() == "1 -> 2 -> 3 -> NULL"