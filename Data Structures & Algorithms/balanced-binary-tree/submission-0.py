# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def dfs(self, node):
        if node is None:
            return 0

        left_height = self.dfs(node.left)
        right_height = self.dfs(node.right)

        if abs(left_height - right_height) > 1:
            self.balanced = False

        return 1 + max(left_height, right_height)

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True

        self.balanced = True

        self.dfs(root)

        return self.balanced
