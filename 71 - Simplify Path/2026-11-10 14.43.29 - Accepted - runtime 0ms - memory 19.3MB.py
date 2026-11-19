class Solution:
    def simplifyPath(self, path):
        stack = []
        for p in path.split('/'):
            if p == '' or p == '.': continue
            if p == '..':
                if stack: stack.pop()
            else:
                stack.append(p)
        return '/' + '/'.join(stack)