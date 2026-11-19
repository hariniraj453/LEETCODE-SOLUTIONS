class Solution:
    def digitSum(self, s: str, k: int) -> str:
        while len(s) > k:
            new_s = ""
            for i in range(0, len(s), k):
                g= s[i:i+k]
                t = sum(int(d) for d in g)
                new_s += str(t)
            s = new_s
        return s