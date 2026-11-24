# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, inorder: list[int], postorder: list[int]) -> 'TreeNode':
        mp = {val: i for i, val in enumerate(inorder)}
        self.post_idx = len(postorder) - 1

        def build(l, r):
            if l > r:
                return None

            root_val = postorder[self.post_idx]
            self.post_idx -= 1
            root = TreeNode(root_val)

            mid = mp[root_val]
            root.right = build(mid + 1, r)
            root.left = build(l, mid - 1)
            return root

        return build(0, len(inorder) - 1)