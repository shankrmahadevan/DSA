class Node:
    def __init__(self, value):
        self.value = value
        self.left_child = None
        self.right_child = None

    def hasLeftChild(self):
        return self.left_child is not None

    def hasRightChild(self):
        return self.right_child is not None


class BinaryTree:
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

    def find(self, value):
        current = self.root
        while current:
            if current.value < value:
                current = current.right_child
            elif current.value > value:
                current = current.left_child
            else:
                return True
        return False


tree = BinaryTree()
for i in [7, 3, 4, 9, 10]:
    tree.insert(i)
