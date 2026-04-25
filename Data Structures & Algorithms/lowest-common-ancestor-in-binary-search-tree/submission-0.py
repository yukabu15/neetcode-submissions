# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        small, large = min(p.val, q.val), max(p.val, q.val)
        stack = deque()
        stack.appendleft(root)

        while deque:
            node = stack.pop()
            node_val = node.val
            if node_val > large:
                stack.appendleft(node.left)
            elif node_val < small:
                stack.appendleft(node.right)
            else:
                return node