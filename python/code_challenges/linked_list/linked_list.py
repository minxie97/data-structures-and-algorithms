class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


class LinkedList:
    def __init__(self, head=None):
        self.head = head
    
    def insert(self, value):
        node = Node(value)
        if self.head is not None:
            node.next = self.head
        self.head = node

    def includes(self, value):
        current = self.head
        while current != None:
            if current.value == value:
                return True
            current = current.next
        return False

    def to_string(self):
        value_string = ""
        node = self.head
        while node != None:
            value_string += f"{node.value} -> "
            node = node.next
        value_string += "NULL"
        return value_string
