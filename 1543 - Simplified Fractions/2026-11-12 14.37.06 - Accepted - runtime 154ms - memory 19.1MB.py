class Solution:
    def simplifiedFractions(self, n):
        res = []
        for d in range(2, n+1):
            for num in range(1, d):
                if all(num%k or d%k for k in range(2, num+1)):
                    res.append(f"{num}/{d}")
        return res