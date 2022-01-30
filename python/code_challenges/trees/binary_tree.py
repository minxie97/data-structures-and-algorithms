from node import Node

class BinaryTree:

    def __init__(self, root=None):
        if root:
            self.root = Node(root)
        else:
            self.root = root

    def pre_order(self):
        values = []

        def walk(root):
            if root is None:
                return
            values.append(root.value)
            walk(root.left)
            walk(root.right)
        if self.root is None:    
            raise(Exception("The tree is empty!"))
        else: 
            walk(self.root)
            return values

    def in_order(self):
        values = []

        def walk(root):
            if root is None:
                return
            walk(root.left)
            values.append(root.value)
            walk(root.right)
        
        if self.root is None:    
            raise(Exception("The tree is empty!"))
        else: 
            walk(self.root)
            return values

    def post_order(self):
        values = []

        def walk(root):
            if root is None:
                return
            walk(root.left)
            walk(root.right)
            values.append(root.value)
        
        if self.root is None:    
            raise(Exception("The tree is empty!"))
        else: 
            walk(self.root)
            return values

class BinarySearchTree(BinaryTree):

    def __init__(self, tree):
        self.tree = tree

    def add(self, value):
        def walk(root):
            if value < root.value:
                if root.left is None:
                    root.left = Node(value)
                else:
                    walk(root.left)
            elif value > root.value:
                if root.right is None:
                    root.right = Node(value)
                else:
                    walk(root.right)
        if self.tree.root:
            walk(self.tree.root)
        else:
            self.tree.root = Node(value)
    
    def contains(self, value):
        def walk(root):
            if root:
                if value == root.value:
                    return True
                elif value < root.value:
                    return walk(root.left)
                elif value > root.value:
                    return walk(root.right)
            else:
                return False
                
        return walk(self.tree.root)
