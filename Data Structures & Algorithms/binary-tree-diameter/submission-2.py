# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def recursive(self, node):
        if node is None:
            return 0

        left_depth = self.recursive(node.left)
        right_depth = self.recursive(node.right)

        self.ans = max(self.ans, left_depth + right_depth)

        return max(left_depth, right_depth) + 1


    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.ans = 0
        self.recursive(root)
        return self.ans

        
        