from node import Node

class Stack:
    def __init__(self, top=None):
        self.top = top

    def push(self, value):
        node = Node(value)
        if self.top is not None:
            node.next = self.top
        self.top = node

    def pop(self): 
        if self.is_empty() is False:
            popping = self.top
            self.top = popping.next
            popping.next = None
            return popping.value
        else:
            raise Exception("Cannot pop an empty stack!")

    def peek(self):
        if self.is_empty() is False:
            return self.top.value
        else:
            raise Exception("Cannot peek an empty stack!")
    
    def is_empty(self):
        return self.top == None