# Construct Node


class Node:
    def __init__(self, d):
        self.data = d
        self.left = None
        self.right = None

# Recursive Tree Search


def recursiveTreeSearch(root, k):

    if not root:
        return None
    elif root.data == k:
        return root

    if k < root.data:
        return recursiveTreeSearch(root.left, k)
    elif k > root.data:
        return recursiveTreeSearch(root.right, k)


# Iterative Tree Search


def iterativeTreeSearch(root, k):
    while root != None and k != root.data:
        if k < root.data:
            root = root.left
        else:
            root = root.right
    return root


root = Node(8)
root.left = Node(3)
root.left.left = Node(1)
root.left.right = Node(6)
root.left.right.left = Node(4)
root.left.right.right = Node(7)
root.right = Node(10)
root.right.right = Node(14)
root.right.right.left = Node(13)

print("---- Search Tree ----")
result_recursiveTreeSearch = recursiveTreeSearch(root, 13)
if result_recursiveTreeSearch != None:
    print(f"Key {result_recursiveTreeSearch.data} is present")
else:
    print("Key not found")

print("---- Iterative Search Tree ----")
result_IterativeSearchTree = iterativeTreeSearch(root, 10)
if result_IterativeSearchTree != None:
    print(f"Key {result_IterativeSearchTree.data} is present")
else:
    print("Key not found")
