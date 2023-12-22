# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        def dfs(root):
            if root is None:
                return []
            elif root.right is None and root.left is None:
                return [root.val]
            leaves = dfs(root.right) + dfs(root.left)
            return leaves
        return dfs(root1) == dfs(root2)
        