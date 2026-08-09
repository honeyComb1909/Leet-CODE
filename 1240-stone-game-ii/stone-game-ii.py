class Solution:
    def stoneGameII(self, piles):
        n = len(piles)

        # Suffix sum
        suffix = [0] * (n + 1)

        for i in range(n - 1, -1, -1):
            suffix[i] = suffix[i + 1] + piles[i]

        memo = {}

        def dp(i, m):
            # Can take all remaining piles
            if i + 2 * m >= n:
                return suffix[i]

            if (i, m) in memo:
                return memo[(i, m)]

            best = 0

            # Try taking 1 to 2*m piles
            for x in range(1, 2 * m + 1):
                # Stones Alice can get =
                # total remaining - maximum Bob can get
                best = max(
                    best,
                    suffix[i] - dp(i + x, max(m, x))
                )

            memo[(i, m)] = best
            return best

        return dp(0, 1)