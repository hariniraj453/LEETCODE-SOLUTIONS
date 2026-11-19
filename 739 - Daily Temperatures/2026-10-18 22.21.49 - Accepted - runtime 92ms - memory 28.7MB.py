class Solution:
    def dailyTemperatures(self, T: list[int]) -> list[int]:
        res = [0]*len(T)
        st = [] # idx
        for i, t in enumerate(T):
            while st and T[st[-1]] < t:
                j = st.pop()
                res[j] = i-j
            st.append(i)
        return res