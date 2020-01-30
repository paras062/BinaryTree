# Construct Node


class Node:
    def __init__(self, d):
        self.data = d
        self.left = None
        self.right = None


def DeleteNode(root, data, flag):
    if not root:
        return None
    elif (data < root.data):
        flag = False
        root.left = DeleteNode(root.left, data, flag)
    elif (data > root.data):
        flag = False
        root.right = DeleteNode(root.right, data, flag)

    # Found node to be deleted
    # CASE 1: Delete root of the binary tree
    elif (data == root.data and flag):
        temp = root
        newRoot = root.left
        root = root.left

        # Move current root to the end of right most node of the left subtree
        while(root.right != None):
            root = root.right

        if root.right == None:
            root.right = temp.right

        del temp, root
        return newRoot
    else:
        # CASE 2: No Child
        if(root.left == None and root.right == None):
            del root
            root = None

        # CASE 3: One Child
        elif (root.left == None):
            temp = root
            root = root.left
            del temp

        # CASE 4: Two Child
        else:
            temp = Node(0)
            temp.data = minValue(root.right, data)
            root.data = temp.data
            root.right = DeleteNode(root.right, temp.data, flag)
    return root


def minValue(node, data):
    current = node
    if (data < node.data):
        # loop down to find the right most leaf
        while(current.right is not None):
            current = current.right
    elif (data > node.data):
        # loop down to find the left most leaf
        while(current.left is not None):
            current = current.left

    return current.data


def DisplayBinaryTree(root):
    if not root:
        return
    DisplayBinaryTree(root.left)
    print("{} ".format(root.data), end="")
    DisplayBinaryTree(root.right)

# Insert value in binary tree


def InsertData(root, data):
    if root == None:
        root = Node(object)
        root.data = data
        root.left = None
        root.right = None
    elif(data <= root.data):
        root.left = InsertData(root.left, data)
    else:
        root.right = InsertData(root.right, data)

    return root


# root = Node(12)
# root.left = Node(5)
# root.left.left = Node(3)
# root.left.left.left = Node(1)
# root.left.right = Node(7)
# root.left.right.right = Node(9)
# root.right = Node(15)
# root.right.left = Node(13)
# root.right.right = Node(17)
root = None
root = InsertData(root, 12)
root = InsertData(root, 5)
root = InsertData(root, 3)
root = InsertData(root, 1)
root = InsertData(root, 7)
root = InsertData(root, 9)
root = InsertData(root, 15)
root = InsertData(root, 13)
root = InsertData(root, 17)

# This flag variable is to judge if node being deleted is the root node.
flag = True
print("--- Tree Before Node Deletion ----")
DisplayBinaryTree(root)
print("\n----------------------------------")
print("Deleting Node.....................")
result = DeleteNode(root, 12, flag)

print("--- Tree After Node Deletion ----")
DisplayBinaryTree(result)
print("\n----------------------------------")

del root
