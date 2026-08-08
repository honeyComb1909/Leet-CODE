class Solution:
    def firstMissingPositive(self, nums):
        n = len(nums)

        # Put each positive number x at index x - 1
        for i in range(n):
            while 1 <= nums[i] <= n and nums[nums[i] - 1] != nums[i]:
                correct_index = nums[i] - 1
                nums[i], nums[correct_index] = nums[correct_index], nums[i]

        # Find the first position where the number is incorrect
        for i in range(n):
            if nums[i] != i + 1:
                return i + 1

        # All numbers 1 to n are present
        return n + 1