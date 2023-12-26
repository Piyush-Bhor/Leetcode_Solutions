# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        def dfs(node, current_sum, path_sum_dict):
            if not node:
                return 0
            
            current_sum += node.val
            count = path_sum_dict.get(current_sum - targetSum, 0)
            path_sum_dict[current_sum] = path_sum_dict.get(current_sum, 0) + 1

            count += dfs(node.left, current_sum, path_sum_dict)
            count += dfs(node.right, current_sum, path_sum_dict)

            path_sum_dict[current_sum] -= 1 

            return count
        
        path_sum_dict = {0:1}
        return dfs(root, 0, path_sum_dict)