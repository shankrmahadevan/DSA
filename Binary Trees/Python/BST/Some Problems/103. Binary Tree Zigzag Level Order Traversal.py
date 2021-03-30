# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.temp = []
        self.result = []

    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        for i in range(self.height(root)+1):
            if i%2==0:
                self.zigzageven(root, i)
            else:
                self.zigzagodd(root, i)
            self.result.append(list(self.temp))
            self.temp = []
        for i in self.result:
            if not i:
                return []
        return self.result

    def height(self, root):
        if root is None:
            return 0
        if root.right is None and root.left is None:
            return 0
        left = self.height(root.left)
        right = self.height(root.right)
        return 1 + max(left, right)

    def zigzagodd(self, root, distance):
        if root is None:
            return
        if distance == 0:
            self.temp.append(root.val)
        self.zigzagodd(root.right, distance-1)
        self.zigzagodd(root.left, distance-1)

    def zigzageven(self, root, distance):
        if root is None:
            return
        if distance == 0:
            self.temp.append(root.val)
        self.zigzageven(root.left, distance-1)
        self.zigzageven(root.right, distance-1)


        