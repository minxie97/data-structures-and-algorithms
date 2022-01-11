from stack import Stack
from queue import Queue
import pytest

def test_push():
    test = Stack()
    test.push(1)
    assert test.top.value == 1
    assert test.is_empty() == False
    assert test.peek() == 1
    
def test_push_multiple():
    test = Stack()
    test.push(1)
    test.push(2)
    test.push(3)
    assert test.top.value == 3
    assert test.is_empty() == False
    assert test.peek() == 3

def test_pop():
    test = Stack()
    test.push(1)
    test.push(2)
    test.push(3)
    assert test.is_empty() == False
    assert test.peek() == 3
    assert test.pop() == 3
    assert test.peek() == 2

def test_empty_whole_stack():
    test = Stack()
    test.push(1)
    test.push(2)
    test.push(3)
    assert test.is_empty() == False
    test.pop()
    test.pop()
    test.pop()
    assert test.is_empty() == True

def test_peek_stack():
    test = Stack()
    test.push(1)
    test.push(2)
    test.push(3)
    assert test.peek() == 3
    test.pop()
    assert test.peek() == 2
    test.pop()
    assert test.peek() == 1

def test_empty_stack():
    test = Stack()
    assert test.top == None
    assert test.is_empty() == True

def test_stack_exceptions():
    test = Stack()
    assert test.top == None
    assert test.is_empty() == True
    with pytest.raises(Exception) as pop_empty_stack:
        test.pop()
    assert str(pop_empty_stack.value) == "Cannot pop an empty stack!"
    with pytest.raises(Exception) as peek_empty_stack:
        test.peek()
    assert str(peek_empty_stack.value) == "Cannot peek an empty stack!"

def test_enqueue():
    test = Queue()
    test.enqueue(1)
    assert test.front.value == 1
    assert test.back.value == 1

def test_multiple_enqueue():
    test = Queue()
    test.enqueue(1)
    test.enqueue(2)
    test.enqueue(3)
    assert test.front.value == 1
    assert test.front.next.value == 2
    assert test.back.value == 3

def test_dequeue():
    test = Queue()
    test.enqueue(1)
    test.enqueue(2)
    test.enqueue(3)
    assert test.front.value == 1
    assert test.dequeue() == 1
    assert test.front.value == 2


def test_peek_queue():
    test = Queue()
    test.enqueue(1)
    test.enqueue(2)
    test.enqueue(3)
    assert test.peek() == 1
    test.dequeue()
    assert test.peek() == 2

def test_dequeue_multiple():
    test = Queue()
    test.enqueue(1)
    test.enqueue(2)
    test.enqueue(3)
    assert test.front.value == 1
    assert test.back.value == 3
    test.dequeue()
    test.dequeue()
    test.dequeue()
    assert test.front == None
    assert test.back == None
    assert test.is_empty() == True

def test_empty_queue():
    test = Queue()
    assert test.front == None
    assert test.back == None
    assert test.is_empty() == True

def test_queue_exceptions():
    test = Queue()
    with pytest.raises(Exception) as dequeue_empty_queue:
        test.dequeue()
    assert str(dequeue_empty_queue.value) == "Cannot dequeue an empty queue!"
    with pytest.raises(Exception) as peek_empty_queue:
        test.peek()
    assert str(peek_empty_queue.value) == "Cannot peek an empty queue!"