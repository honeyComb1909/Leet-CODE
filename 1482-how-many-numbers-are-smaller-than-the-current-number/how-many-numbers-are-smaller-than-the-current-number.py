class Solution:
    def smallerNumbersThanCurrent(self, nums):
        ans = []

        for num in nums:
            count = 0

            for x in nums:
                if x < num:
                    count += 1

            ans.append(count)

        return ans