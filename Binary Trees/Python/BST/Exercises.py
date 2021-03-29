class Node:
    def __init__(self, value):
        self.value = value
        self.left_child = None
        self.right_child = None

    def hasLeftChild(self):
        return self.left_child is not None

    def hasRightChild(self):
        return self.right_child is not None

    def isLeafNode(self):
        return not (self.hasLeftChild() or self.hasRightChild())

    def isValid(self):
        return self is not None


class BinarySearchTree:
    def __init__(self):
        self.root = Node(None)

    def insert(self, value):
        if not self.root.value:
            self.root.value = value
        else:
            current = self.root
            node = Node(value)
            while True:
                if current.value < value:
                    if not current.hasRightChild():
                        current.right_child = node
                        break
                    current = current.right_child
                else:
                    if not current.hasLeftChild():
                        current.left_child = node
                        break
                    current = current.left_child

    def contains(self, value):
        current = self.root
        while current:
            if current.value < value:
                current = current.right_child
            elif current.value > value:
                current = current.left_child
            else:
                return True
        return False

    def equals(self, root1, root2):
        if root1 is None and root2 is None:
            return True
        elif root1 is not None and root2 is not None:
            left = self.equals(root1.left_child, root2.left_child)
            right = self.equals(root1.right_child, root2.right_child)
            return root1.value == root2.value and left and right
        return False

    def __eq__(self, other):
        return self.equals(self.root, other.root)


# 1. Find the Height of a Binary Tree
def height(root):
    if root is None:
        return 0
    if root.isLeafNode():
        return 0
    left = height(root.left_child)
    right = height(root.right_child)
    return 1 + max(left, right)


# 2. Write a function to find whether a Binary Search tree is valid.
def isValidBST(root, max_val, min_val):
    if root is None:
        return True
    if min_val < root.value < max_val:
        return isValidBST(root.left_child, root.value, min_val) and isValidBST(root.right_child, max_val, root.value)
    else:
        return False


# 3. Find the min value in a Binary Tree (Not BST)
def min_value(root):
    if root is None:
        return float('inf')
    if root.isLeafNode():
        return root.value
    left = min_value(root.left_child)
    right = min_value(root.right_child)
    return min(min(left, right), root.value)


# 4. Find the Max value of a binary Tree:
def max_value(root):
    if root is None:
        return float('-inf')
    if root.isLeafNode():
        return root.value
    left = max_value(root.left_child)
    right = max_value(root.right_child)
    return max(max(left, right), root.value)


# 5. Count the number of leaves in the tree.
def NumberOfLeaves(root):
    if root is None:
        return 0
    if root.isLeafNode():
        return 1
    return NumberOfLeaves(root.left_child) + NumberOfLeaves(root.right_child)


# 6. Get the Ancestors of a node.
def getAncestors(root, number, output_list):
    if root is None:
        return False
    if root.value == number:
        return True
    if getAncestors(root.left_child, number, output_list) or getAncestors(root.right_child, number, output_list):
        output_list.append(root.value)
    return output_list


tree = BinarySearchTree()
for i in [71, 4, 9, 1, 6, 8, 10]:
    tree.insert(i)
print(height(tree.root))
print(min_value(tree.root))
print(max_value(tree.root))
print(isValidBST(tree.root, float('inf'), float('-inf')))
print(NumberOfLeaves(tree.root))
print(getAncestors(tree.root, 8, []))
