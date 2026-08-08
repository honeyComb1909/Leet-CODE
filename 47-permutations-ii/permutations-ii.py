class Solution:
    def permuteUnique(self, nums):
        result = []
        nums.sort()
        used = [False] * len(nums)

        def backtrack(current):
            # Complete permutation
            if len(current) == len(nums):
                result.append(current[:])
                return

            for i in range(len(nums)):

                # Already used
                if used[i]:
                    continue

                # Skip duplicates
                if i > 0 and nums[i] == nums[i - 1] and not used[i - 1]:
                    continue

                used[i] = True
                current.append(nums[i])

                backtrack(current)

                current.pop()
                used[i] = False

        backtrack([])
        return result