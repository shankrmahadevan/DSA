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


def in_order_traversal(root):
    # Left, root, right.
    # Create a stack. Keep appending left nodes until There are none left.
    # Now, the left most node is at the end of the stack.
    # pop it out, add its value to the result array.
    # if this popped out current element has a right child,
    # set current to the right child.
    # if --> that right child has a left child, it will get added to the stack.
    # else --> it will again add the value in the root since the current is None (no right child)
    # Iterate till stack is empty and no more nodes remain.
    stack, result = [], []
    current = root
    while True:
        if current is not None:
            stack.append(current)
            current = current.left_child
        elif stack:
            current = stack.pop()
            result.append(current.value)
            current = current.right_child
        else:
            break
    return result


def post_order_traversal(root):
    stack, result = [], []
    current = root
    while True:
        if current is not None:
            stack.append(current)
            if current.right_child is not None:
                stack.append(current.right_child)
            current = current.left_child
        elif stack:
            current = stack.pop()
            result.append(current.value)
            current = current.right_child
        else:
            break
    return result


tree = BinarySearchTree()
for i in [7, 4, 9, 1, 6, 8, 10]:
    tree.insert(i)
print(in_order_traversal(tree.root))
print(post_order_traversal(tree.root))
