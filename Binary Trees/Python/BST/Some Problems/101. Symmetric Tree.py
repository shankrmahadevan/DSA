# Node.value;Node.left_child;Node.right_child
def is_symmetric(root1, root2):
    if root1 is None and root2 is None:
        return True
    elif root1 is None or root2 is None:
        return False
    return root1.value == root2.value and is_symmetric(root1.right, root2.left) and is_symmetric(root1.left, root2.right)
