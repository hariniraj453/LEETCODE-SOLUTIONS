class Solution:
    def findMedianSortedArrays(self, a: list[int], b: list[int]) -> float:
        if len(a) > len(b): a,b = b,a
        n, m = len(a), len(b)
        l, r = 0, n
        while l <= r:
            i = (l+r)//2
            j = (n+m+1)//2 - i
            al = a[i-1] if i>0 else float('-inf')
            ar = a[i] if i<n else float('inf')
            bl = b[j-1] if j>0 else float('-inf')
            br = b[j] if j<m else float('inf')
            if al <= br and bl <= ar:
                if (n+m)%2: return max(al, bl)
                return (max(al,bl)+min(ar,br))/2
            elif al > br: r=i-1
            else: l=i+1