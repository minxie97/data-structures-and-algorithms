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

    def append(self, value):
        current = self.head
        if current:
            while current.next != None:
                current = current.next
            current.next = Node(value)
        else:
            self.head = Node(value)

    def insert_before(self, search_value, new_value):
        if self.head.value == search_value:
            node = Node(new_value)
            node.next = self.head
            self.head = node
        else: 
            current = self.head
            while current.next != None:
                if current.next.value == search_value:
                    temp = current.next
                    current.next = Node(new_value, temp)
                    break
                current = current.next

    def insert_after(self, search_value, new_value):
        current = self.head
        while current != None:
            if current.value == search_value:
                temp = current.next
                current.next = Node(new_value, temp)
                break
            current = current.next
