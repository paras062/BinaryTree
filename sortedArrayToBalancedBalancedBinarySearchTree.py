# Python Code to convert sorted array to Binary Search Tree
# Binary tree Node


class Node:
    def __init__(self, d):
        self.data = d
        self.left = None
        self.right = None

# Function to convert sorted array to Binary Tree


def sortedArrayToBST(arr):
    if not arr:
        return None

    # Find mid element
    mid_element = int((len(arr))/2)

    # make mid element root
    root = Node(arr[mid_element])

    # left subtree has all values < arr[mid_element]

    # here colon (:) before mid_element specifies everything before & including index mid_element
    root.left = sortedArrayToBST(arr[:mid_element])

    # right subtree has all values > arr[mid_element]

    # here colon (:) after mid_element specifies everything after index mid_element, but not including mid_element
    root.right = sortedArrayToBST(arr[mid_element+1:])

    return root


# Traversal of BST

# Pre Order - PLR
def preOrder(node):
    if not node:
        return None

    print(node.data)
    preOrder(node.left)
    preOrder(node.right)


# In Order - LPR
def inOrder(node):
    if not node:
        return None

    inOrder(node.left)
    print(node.data)
    inOrder(node.right)


# Post Order - LRP
def postOrder(node):
    if not node:
        return None

    postOrder(node.left)
    postOrder(node.right)
    print(node.data)


arr = [1, 2, 3, 4, 5, 6, 7, 8]
root = sortedArrayToBST(arr)
print("Pre Order")
preOrder(root)

print("In Order")
inOrder(root)

print("Post Order")
postOrder(root)
