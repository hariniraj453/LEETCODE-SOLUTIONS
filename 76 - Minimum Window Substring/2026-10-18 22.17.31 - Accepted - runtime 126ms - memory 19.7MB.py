class Solution:
    def minWindow(self, s: str, t: str) -> str:
        need = {}
        for c in t: need[c] = need.get(c,0)+1
        have = {}
        need_len = len(need)
        have_len = 0
        l = 0
        res = ""
        res_len = float('inf')
        for r in range(len(s)):
            c = s[r]
            have[c] = have.get(c,0)+1
            if c in need and have[c]==need[c]:
                have_len+=1
            while have_len==need_len:
                if r-l+1 < res_len:
                    res = s[l:r+1]
                    res_len = r-l+1
                have[s[l]]-=1
                if s[l] in need and have[s[l]] < need[s[l]]:
                    have_len-=1
                l+=1
        return res