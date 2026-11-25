class Solution:
    def rotate(self, nums, k):
        n = len(nums)
        k %= n
        
        def reverse(l, r):
            while l < r:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
                r -= 1
        
        reverse(0, n-1)   # Full reverse
        reverse(0, k-1)   # First k reverse
        reverse(k, n-1)   # Micham reverse