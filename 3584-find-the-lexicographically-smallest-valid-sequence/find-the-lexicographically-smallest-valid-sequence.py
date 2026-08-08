class Solution:
    def validSequence(self, word1: str, word2: str) -> list[int]:
        n = len(word1)
        m = len(word2)

        # last[j] = last index in word1 where word2[j] can be matched
        last = [-1] * m

        i = n - 1
        j = m - 1

        while i >= 0 and j >= 0:
            if word1[i] == word2[j]:
                last[j] = i
                j -= 1
            i -= 1

        ans = []
        j = 0
        can_change = True

        for i in range(n):
            if j == m:
                break

            # Exact match
            if word1[i] == word2[j]:
                ans.append(i)
                j += 1

            # Use the one allowed mismatch
            elif can_change:
                # We can change word1[i] only if the remaining
                # part of word2 can still be matched afterward.
                if j == m - 1 or i < last[j + 1]:
                    ans.append(i)
                    j += 1
                    can_change = False

        return ans if j == m else []