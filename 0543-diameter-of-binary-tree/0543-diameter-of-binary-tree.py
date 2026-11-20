class Solution:
    def diameterOfBinaryTree(self, root):
        ans = [0]
        def dfs(node):
            if not node:
                return 0
            l = dfs(node.left)
            r = dfs(node.right)
            ans[0] = max(ans[0], l + r)
            return 1 + max(l, r)
        dfs(root)
        return ans[0]