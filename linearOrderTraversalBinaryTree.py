import queue

# Construct Node


class Node:
    def __init__(self, d):
        self.data = d
        self.left = None
        self.right = None

# Method to create level order tree


def LevelOrderTree(root):
    if not root:
        return None

    # Defining Queue
    Q = queue.Queue(maxsize=30)
    Q.put(root)

    while not Q.empty():
        current = Q.get()
        print(current.data)
        if current.left != None:
            Q.put(current.left)

        if current.right != None:
            Q.put(current.right)
    
    # Release memory after program execution
    del Q, current

# Inputs

# ********** TEST CASE 1 **********
#           M
#         /    \
#       B        Q
#      /  \        \
#     A     C        Z

# ********** Uncomment below code to run test case 1 **********
# root = Node('M')
# root.left = Node('B')
# root.right = Node('Q')
# root.left.left = Node('A')
# root.left.right = Node('C')
# root.right.right = Node('Z')


# ********** TEST CASE 2 **********
#                     F
#                   /   \
#                 /       \
#               /          \
#              D            J
#           /     \       /   \
#          B        E    G     K
#        /   \             \
#       A     C              I
#                           /
#                          H

# ********** Uncomment below code to run the test case 2 **********

# Inserting values into the nodes.
root = Node('F')
root.left = Node('D')
root.left.left = Node('B')
root.left.right = Node('E')
root.left.left.left = Node('A')
root.left.left.right = Node('C')
root.right = Node('J')
root.right.left = Node('G')
root.right.right = Node('K')
root.right.left.right = Node('I')
root.right.left.right.left = Node('H')

# Passing root to LevelOrderTree method
LevelOrderTree(root)

# Releae memory after program execution
del root