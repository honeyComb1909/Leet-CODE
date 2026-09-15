class Solution:
    def maxPalindromes(self, s: str, k: int) -> int:
        n = len(s)

        # pal[i][j] = True if s[i:j+1] is a palindrome
        pal = [[False] * n for _ in range(n)]

        for i in range(n - 1, -1, -1):
            for j in range(i, n):
                if s[i] == s[j] and (j - i <= 1 or pal[i + 1][j - 1]):
                    pal[i][j] = True

        dp = [0] * (n + 1)

        for i in range(1, n + 1):
            dp[i] = dp[i - 1]

            if i >= k and pal[i - k][i - 1]:
                dp[i] = max(dp[i], dp[i - k] + 1)

            if i >= k + 1 and pal[i - k - 1][i - 1]:
                dp[i] = max(dp[i], dp[i - k - 1] + 1)

        return dp[n]