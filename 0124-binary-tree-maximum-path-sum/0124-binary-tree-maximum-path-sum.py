# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root) -> int:
        self.max_sum = float('-inf')

        def dfs(node):
            if not node:
                return 0
            
            # Negative na 0 eduthuko, venam
            left = max(dfs(node.left), 0)
            right = max(dfs(node.right), 0)
            
            # 1. Idhu oru full path ah irundha evlo?
            current_path = node.val + left + right
            
            # Global max update pannu
            self.max_sum = max(self.max_sum, current_path)
            
            # 2. Appa ku oru side mattum return pannu
            return node.val + max(left, right)

        dfs(root)
        return self.max_sum