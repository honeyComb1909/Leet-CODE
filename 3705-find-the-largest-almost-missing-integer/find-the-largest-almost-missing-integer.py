class Solution:
    def largestInteger(self, nums, k):
        n = len(nums)
        cnt = {}

        for i in range(n - k + 1):
            seen = set(nums[i:i + k])
            for x in seen:
                cnt[x] = cnt.get(x, 0) + 1

        ans = -1
        for x in cnt:
            if cnt[x] == 1:
                ans = max(ans, x)

        return ans