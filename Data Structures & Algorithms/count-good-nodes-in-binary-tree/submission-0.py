# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if not root:
            return 0
        self.count = 0

        def dfs_helper(node, max_so_far):
            if not node:
                return
            if node.val >= max_so_far:
                self.count += 1
                max_so_far = node.val
            
            dfs_helper(node.left, max_so_far)
            dfs_helper(node.right, max_so_far)

        dfs_helper(root, root.val)

        return self.count
        