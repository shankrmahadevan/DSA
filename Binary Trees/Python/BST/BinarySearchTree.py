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


tree = BinarySearchTree()
for i in [7, 4, 9, 1, 6, 8, 10]:
    tree.insert(i)
