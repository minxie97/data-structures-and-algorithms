def breadth_first(tree):
    if tree.root is None:
        raise(Exception("The tree is empty!"))

    queue = [tree.root]
    result = []
    while len(queue) > 0:
    
        current = queue.pop(0)
        result.append(current.value)

        if current.left:
            queue.append(current.left)
        if current.right:
            queue.append(current.right)

    return result

def breadth_first_reverse(tree):
    if tree.root is None:
        raise(Exception("The tree is empty!"))

    queue = [tree.root]
    stack = []
    while len(queue) > 0:
    
        current = queue.pop(0)
        stack.append(current.value)

        if current.left:
            queue.append(current.left)
        if current.right:
            queue.append(current.right)

    while stack:
        print(stack.pop())


    

