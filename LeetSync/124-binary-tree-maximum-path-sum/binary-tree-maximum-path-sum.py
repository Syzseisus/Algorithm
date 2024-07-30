# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.max_sum = float('-inf')  # Initialize to the smallest possible value
        
        def dfs(node: Optional[TreeNode]) -> int:
            if not node:
                return 0  # Base case: null node contributes 0 to the path sum
            
            # Recursively compute the maximum path sum of the left and right subtrees
            left_max = max(dfs(node.left), 0)  # Ignore paths with negative sums
            right_max = max(dfs(node.right), 0)  # Ignore paths with negative sums
            
            # Compute the path sum that passes through the current node
            current_path_sum = node.val + left_max + right_max
            
            # Update the maximum path sum found so far
            self.max_sum = max(self.max_sum, current_path_sum)
            
            # Return the maximum path sum that can be extended to the parent
            return node.val + max(left_max, right_max)
        
        dfs(root)  # Start DFS from the root
        return self.max_sum  # Return the maximum path sum found
