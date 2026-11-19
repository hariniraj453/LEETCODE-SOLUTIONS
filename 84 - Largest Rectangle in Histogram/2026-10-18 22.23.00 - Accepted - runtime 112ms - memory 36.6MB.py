class Solution:
    def largestRectangleArea(self, h: list[int]) -> int:
        st = [] # (idx, height)
        maxA = 0
        for i, ht in enumerate(h):
            start = i
            while st and st[-1][1] > ht:
                idx, he = st.pop()
                maxA = max(maxA, he*(i-idx))
                start = idx
            st.append((start, ht))
        for idx, he in st:
            maxA = max(maxA, he*(len(h)-idx))
        return maxA