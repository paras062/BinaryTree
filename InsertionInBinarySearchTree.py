# Construct Node


class Node:
    def __init__(self, d):
        self.data = d
        self.left = None
        self.right = None


# Node to be inserted
class NodeToBeInserted:
    def __init__(self, d):
        self.parent = None
        self.data = d
        self.left = None
        self.right = None


def InsertNewNode(root, newNode):
    y = None
    z = newNode
    while root != None:
        y = root
        if z.data < root.data:
            root = root.left
        else:
            root = root.right
        z.parent = y

    if y == None:
        root = z
    elif z.data < y.data:
        y.left = z
    else:
        y.right = z

    DisplayBinaryTree(y)

    # Releae memory after program execution
    del y, z

# Display Binary Tree


def DisplayBinaryTree(root):
    if not root:
        return
    DisplayBinaryTree(root.left)
    print("{} ".format(root.data), end="")
    DisplayBinaryTree(root.right)


root = Node(12)
root.left = Node(5)
root.left.left = Node(2)
root.left.right = Node(9)
root.right = Node(18)
root.right.left = Node(15)
root.right.left.right = Node(17)
root.right.right = Node(19)

z = NodeToBeInserted(13)

InsertNewNode(root, z)

# Releae memory after program execution
del root, z
