from stack import Stack
from queue import Queue
from pseudoqueue import PseudoQueue
from stack_queue_animal_shelter import Cat, Dog, AnimalShelter
from stack_queue_brackets import validate_brackets

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

def test_pseudo_empty():
    test = PseudoQueue()
    assert test.stack1.is_empty() == True
    assert test.stack2.is_empty() == True

def test_pseudo_enqueue():
    test = PseudoQueue()
    test.enqueue(1)
    assert test.stack1.top.value == 1

def test_pseudo_enqueue_multi():
    test = PseudoQueue()
    test.enqueue(1)
    test.enqueue(2)
    test.enqueue(3)
    assert test.stack1.top.value == 1
    assert test.stack1.top.value != 2
    assert test.stack1.top.value != 3

def test_pseudo_dequeue():
    test = PseudoQueue()
    test.enqueue(1)
    assert test.dequeue() == 1

def test_pseudo_dequeue_multi():
    test = PseudoQueue()
    test.enqueue(1)
    test.enqueue(2)
    test.enqueue(3)
    assert test.dequeue() == 1
    assert test.stack1.top.value == 2
    assert test.dequeue() == 2
    assert test.stack1.top.value == 3

def test_pseudo_empty_dequeue():
    test = PseudoQueue()
    with pytest.raises(Exception) as dequeue_empty:
        test.dequeue()
    assert str(dequeue_empty.value) == "The pseudo queue is empty!"

def test_animal_shelter_empty():
    test = AnimalShelter()
    assert test.pets.is_empty() == True
    assert test.holding.is_empty() == True

def test_animal_shelter_enqueue():
    test = AnimalShelter()
    cat = Cat("Jonesy")
    test.enqueue(cat)
    assert test.pets.top.value == cat

def test_animal_shelter_enqueue_multi():
    test = AnimalShelter()
    cat = Cat()
    dog = Dog()
    test.enqueue(cat)
    test.enqueue(dog)
    assert test.pets.top.value == cat
    assert test.pets.top.next.value == dog

def test_animal_shelter_dequeue():
    test = AnimalShelter()
    cat = Cat()
    test.enqueue(cat)
    assert test.dequeue("cat") == cat

def test_animal_shelter_dequeue_multi():
    test = AnimalShelter()
    jonesy = Cat("Jonesy")
    neo = Cat("Neo")
    test.enqueue(jonesy)
    test.enqueue(neo)
    assert test.pets.top.value == jonesy
    assert test.dequeue("cat") == jonesy
    assert test.pets.top.value == neo
    assert test.dequeue("cat") == neo

def test_animal_shelter_dequeue_move_dog():
    test = AnimalShelter()
    dog = Dog()
    cat = Cat()
    test.enqueue(dog)
    test.enqueue(cat)
    assert test.pets.top.value == dog
    assert test.dequeue("cat") == cat
    assert test.pets.top.value == dog

def test_animal_shelter_dequeue_move_multi_dogs():
    test = AnimalShelter()
    dog_one = Dog()
    dog_two = Dog()
    cat = Cat()
    test.enqueue(dog_one)
    test.enqueue(dog_two)
    test.enqueue(cat)
    assert test.pets.top.value == dog_one
    assert test.pets.top.next.value == dog_two
    assert test.dequeue("cat") == cat
    assert test.pets.top.value == dog_one
    assert test.pets.top.next.value == dog_two

def test_animal_shelter_dequeue_not_cat_or_dog():
    test = AnimalShelter()
    dog_one = Dog()
    dog_two = Dog()
    cat = Cat()
    test.enqueue(dog_one)
    test.enqueue(dog_two)
    test.enqueue(cat)
    assert test.pets.top.value == dog_one
    assert test.dequeue("whoever") == dog_one

def test_validate_bracket_true():
    assert validate_brackets("{}") == True
    assert validate_brackets("{}(){}") == True
    assert validate_brackets("(){}[[]]") == True


def test_validate_bracket_false():
    assert validate_brackets("[({}]") == False
    assert validate_brackets("(](") == False
    assert validate_brackets("{(})") == False

def test_validate_bracket_characters_in_brackets():
    assert validate_brackets("()[[words!]]") == True
    assert validate_brackets("{}{Words?}[Words!](())") == True