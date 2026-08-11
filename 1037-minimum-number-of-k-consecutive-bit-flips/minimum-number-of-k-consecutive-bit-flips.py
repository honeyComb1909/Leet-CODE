class Solution:
    def minKBitFlips(self, nums, k):
        n = len(nums)
        diff = [0] * (n + 1)
        flips = 0
        active = 0

        for i in range(n):
            active ^= diff[i]

            if nums[i] ^ active == 0:
                if i + k > n:
                    return -1

                flips += 1
                active ^= 1
                diff[i + k] ^= 1

        return flips