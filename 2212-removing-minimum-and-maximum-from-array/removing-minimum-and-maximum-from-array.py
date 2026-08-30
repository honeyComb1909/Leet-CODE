class Solution:
    def minimumDeletions(self, nums):
        n = len(nums)

        mn = mx = 0

        for i in range(n):
            if nums[i] < nums[mn]:
                mn = i
            if nums[i] > nums[mx]:
                mx = i

        left = min(mn, mx)
        right = max(mn, mx)

        # 1. Both from front
        front = right + 1

        # 2. Both from back
        back = n - left

        # 3. One from front, one from back
        both = (left + 1) + (n - right)

        return min(front, back, both)