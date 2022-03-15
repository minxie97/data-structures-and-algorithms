class Node:
    def __init__(self, key, value, next=None):
        self.key = key
        self.value = value
        self.next = next

class HashTable:
    def __init__(self, size=1024):
        self.size = size
        self.table = [None] * size
        self.allkeys = set()

    def set(self, key, value):
        if key not in self.allkeys:
            index = self.hash(key)
            if self.table[index] is None:
                self.table[index] = Node(key, value)
            else:
                node = self.table[index]
                while node.next:
                    node = node.next
                node.next = Node(key, value)
            self.allkeys.add(key)
        else:
            return
    
    def get(self, key):
        if key not in self.allkeys:
            return None
        else:
            index = self.hash(key)
            node = self.table[index]
            if node.key == key:
                return node.value
            else:
                while node.next:
                    node = node.next
                    if node.key == key:
                        return node.value
                

    def contains(self, key):
        return key in self.allkeys

    def keys(self):
        return list(self.allkeys)

    def hash(self, key):
        return sum([ord(char) for char in key]) * 599 % self.size