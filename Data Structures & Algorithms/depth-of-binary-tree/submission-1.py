# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root == None:
            return 0
        max_depth = 0
        curr_depth = 0
        queue = deque([[root, 1]])

        while queue:
            pair = queue.pop()
            node, cur_depth = pair[0], pair[1]
            if node.left:
                queue.append([node.left, cur_depth + 1])
            if node.right:
                queue.append([node.right, cur_depth + 1])
            max_depth = max(max_depth, cur_depth)
        
        return max_depth