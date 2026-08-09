class Solution:
    def beautifulArray(self, n):
        result = [1]

        while len(result) < n:
            # Odd numbers
            result = [2 * x - 1 for x in result if 2 * x - 1 <= n] + \
                     [2 * x for x in result if 2 * x <= n]

        return result