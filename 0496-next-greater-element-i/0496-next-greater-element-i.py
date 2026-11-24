class Solution:
    def nextGreaterElement(self, nums1: list[int], nums2: list[int]) -> list[int]:
        mp = {}
        stack = []

        for num in reversed(nums2):
            while stack and stack[-1] <= num:
                stack.pop()

            mp[num] = stack[-1] if stack else -1
            stack.append(num)

        return [mp[x] for x in nums1]