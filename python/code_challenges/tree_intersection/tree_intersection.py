from hashtable.hashtable import HashTable

def tree_intersection(tree1, tree2):
    value_bank = HashTable()
    answers = []
    inorder(value_bank, tree1, answers)
    inorder(value_bank, tree2, answers)
    return answers


def inorder(hashmap, tree, list):
    def walk(root):
        if root is None:
            return
        walk(root.left)
        if hashmap.contains(str(root.value)):
            list.append(root.value)
        else: 
            hashmap.set(str(root.value), None)
        walk(root.right)

    walk(tree.root)

