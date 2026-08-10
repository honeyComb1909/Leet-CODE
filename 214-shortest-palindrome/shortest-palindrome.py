class Solution:
    def shortestPalindrome(self, s: str) -> str:
        rev = s[::-1]

        # Find the longest palindromic prefix using KMP
        combined = s + "#" + rev

        lps = [0] * len(combined)

        for i in range(1, len(combined)):
            j = lps[i - 1]

            while j > 0 and combined[i] != combined[j]:
                j = lps[j - 1]

            if combined[i] == combined[j]:
                j += 1

            lps[i] = j

        longest_prefix = lps[-1]

        # Characters after the palindromic prefix
        remaining = s[longest_prefix:]

        return remaining[::-1] + s