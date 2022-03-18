# Tree Intersection
Find common values in two binary trees

## Whiteboard Process
![tree-intersection-whiteboard](https://github.com/minxie97/data-structures-and-algorithms/blob/tree-intersection/python/code_challenges/tree_intersection/tree_intersection.jpg)

## Approach & Efficiency
My approach was to traverse the first tree and set all the values inside that tree in an empty HashTable. I then traverse the second tree and check if the values in that second tree is already in the HashTable. If so I know that value is a common value and I add that to the return list. If not, I set it inside the HashTable.

## Solution
```
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
```
