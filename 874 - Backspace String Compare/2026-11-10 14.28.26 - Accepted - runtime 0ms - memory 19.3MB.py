class Solution:
    def backspaceCompare(self, s, t):
        def final(st):
            res = []
            for c in st:
                if c == '#': 
                    if res: res.pop()
                else: res.append(c)
            return res
        return final(s) == final(t)