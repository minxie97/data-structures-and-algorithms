from node import Node

class Queue:
    def __init__(self, front=None, back=None):
        self.front = front
        self.back = back

    def enqueue(self, value):
        node = Node(value)
        if self.back is not None:
            self.back.next = node
        self.back = node
        if self.front is None:
            self.front = self.back
    
    def dequeue(self):
        if self.is_empty() is False:
            dequeuing = self.front
            self.front = self.front.next
            if self.front is None:
                self.back = None
            dequeuing.next = None
            return dequeuing.value
        else:
            raise Exception("Cannot dequeue an empty queue!")

    def peek(self):
        if self.is_empty() is False:
            return self.front.value
        else:
            raise Exception("Cannot peek an empty queue!")

    def is_empty(self):
        return self.front == None
