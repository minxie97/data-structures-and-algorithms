class KNode:
    def __init__(self, value=None, children=[]):
        self.value = value
        self.children = children

class KTree:
    def __init__(self, root=None):
        self.root = root
    
    def breadth_first(self):
        queue = [self.root]
        results = []
        while queue:
            temp = queue.pop(0)
            results.append(temp.value)
            queue.extend(temp.children)
        return results

def tree_fizz_buzz(tree):
    def translate(num):
        if num % 3 == 0 and num % 5 == 0:
            return "FizzBuzz"
        elif num % 5 == 0:
            return "Buzz"
        elif num % 3 == 0:
            return "Fizz"
        else:
            return str(num)
    
    def walk(root):
        if root is None:
            return
        root.value = translate(root.value)
        for child in root.children:
            walk(child)

    if tree.root:
        walk(tree.root)
        return tree
    else:
        raise(Exception("The tree is empty!"))
