class AVLNode:
    def __init__(self, value):
        self.value = value
        self.left_child = None
        self.right_child = None
        self.height = 0

    def hasLeftChild(self):
        return self.left_child is not None

    def hasRightChild(self):
        return self.right_child is not None

    def isLeafAVLNode(self):
        return not (self.hasLeftChild() or self.hasRightChild())


class AVLTree:
    def __init__(self):
        self.root = AVLNode(None)

    def insert(self, value):
        if self.root.value is None:
            self.root.value = value
        else:
            self.recursive_insert(self.root, value)

    def recursive_insert(self, root, value):
        if root is None:
            return AVLNode(value)

        if value < root.value:
            root.left_child = self.recursive_insert(root.left_child, value)
        else:
            root.right_child = self.recursive_insert(root.right_child, value)

        root.height = max(self.height(root.left_child), self.height(root.right_child)) + 1

        return root

    def height(self, node):
        return -1 if node is None else node.height


avl_tree = AVLTree()
for i in [7, 4, 9, 1, 6, 8, 10]:
    avl_tree.insert(i)
