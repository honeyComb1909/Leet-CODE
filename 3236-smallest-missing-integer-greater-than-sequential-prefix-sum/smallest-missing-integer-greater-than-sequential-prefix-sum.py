class Solution:
    def missingInteger(self, nums):
        # Find the sequential prefix sum
        total = nums[0]

        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1] + 1:
                total += nums[i]
            else:
                break

        # Store all numbers for quick lookup
        seen = set(nums)

        # Find the smallest missing integer >= total
        while total in seen:
            total += 1

        return total