import math

class Solution:
    def judgeSquareSum(self, c):
        l, r = 0, int(math.sqrt(c))
        while l <= r:
            total = l*l + r*r
            if total == c:
                return True
            elif total < c:
                l += 1
            else:
                r -= 1
        return False