class Solution:
    def isSymmetric(self, root) -> bool:
        def isMirror(l, r):
            if not l and not r:
                return True
            if not l or not r:
                return False
            return l.val == r.val and isMirror(l.left, r.right) and isMirror(l.right, r.left)
        
        return isMirror(root.left, root.right) if root else True