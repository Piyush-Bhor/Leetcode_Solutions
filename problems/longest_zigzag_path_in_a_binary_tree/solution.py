# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        def dfs(node,isLeft,length,max_length):
            if not node:
                return max_length[0]
            max_length[0] = max(max_length[0], length)
            
            if isLeft:
                dfs(node.right,False,length+1,max_length)
                dfs(node.left,True,1,max_length)
            else:
                dfs(node.right,False,1,max_length)
                dfs(node.left,True,length+1,max_length)
            
            return max_length[0]
        
        return dfs(root,True,0,[0])
        