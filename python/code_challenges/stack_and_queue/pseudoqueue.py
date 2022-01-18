from stack import Stack

class PseudoQueue:
    def __init__(self):
        self.stack1 = Stack()
        self.stack2 = Stack()

    def enqueue(self, value):
        while self.stack1.top != None:
            self.stack2.push(self.stack1.pop())
        self.stack1.push(value)
        while self.stack2.top != None:
            self.stack1.push(self.stack2.pop())
        
    def dequeue(self):
        if self.stack1.top != None:
            return self.stack1.pop()
        else: 
            raise Exception("The pseudo queue is empty!")

