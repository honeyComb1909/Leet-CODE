class Solution:
    def lexicographicallySmallestArray(self, nums, limit):
        arr = sorted(zip(nums, range(len(nums))))
        ans = [0] * len(nums)

        i = 0

        while i < len(nums):
            j = i + 1

            # Find all elements that can be connected
            while j < len(nums) and arr[j][0] - arr[j - 1][0] <= limit:
                j += 1

            # Sort their original indices
            indices = sorted(idx for _, idx in arr[i:j])

            # Put smallest values at smallest indices
            for idx, (value, _) in zip(indices, arr[i:j]):
                ans[idx] = value

            i = j

        return ans