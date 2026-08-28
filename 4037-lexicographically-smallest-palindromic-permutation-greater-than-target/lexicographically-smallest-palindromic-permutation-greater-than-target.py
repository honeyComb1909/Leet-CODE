class Solution:
    def lexPalindromicPermutation(self, s: str, target: str) -> str:
        n = len(s)

        cnt = [0] * 26
        for ch in s:
            cnt[ord(ch) - 97] += 1

        # Palindrome possible only with at most one odd count
        if sum(x & 1 for x in cnt) > 1:
            return ""

        half = [x // 2 for x in cnt]
        m = n // 2

        middle = -1
        for i in range(26):
            if cnt[i] & 1:
                middle = i
                break

        def build(left):
            L = ''.join(chr(x + 97) for x in left)
            M = chr(middle + 97) if middle != -1 else ''
            return L + M + L[::-1]

        answer = ""

        # ---------------------------------------------------------
        # CASE 1:
        # Left half == target's left half
        # ---------------------------------------------------------
        used = [0] * 26
        left = []
        possible = True

        for i in range(m):
            c = ord(target[i]) - 97

            if used[c] >= half[c]:
                possible = False
                break

            used[c] += 1
            left.append(c)

        if possible:
            candidate = build(left)

            if candidate > target:
                answer = candidate

        # ---------------------------------------------------------
        # CASE 2:
        # Find the smallest left half STRICTLY greater than
        # target[:m].
        #
        # Change the rightmost possible position, then fill the
        # remaining positions with the smallest characters.
        # ---------------------------------------------------------
        for i in range(m - 1, -1, -1):

            used = [0] * 26
            valid = True

            # Keep target[0:i] unchanged
            for j in range(i):
                c = ord(target[j]) - 97

                if used[c] >= half[c]:
                    valid = False
                    break

                used[c] += 1

            if not valid:
                continue

            cur = ord(target[i]) - 97

            # Smallest character strictly greater than target[i]
            bigger = -1

            for c in range(cur + 1, 26):
                if used[c] < half[c]:
                    bigger = c
                    break

            if bigger == -1:
                continue

            used[bigger] += 1

            new_left = [ord(target[j]) - 97 for j in range(i)]
            new_left.append(bigger)

            # Fill remaining positions as small as possible
            for c in range(26):
                new_left.extend([c] * (half[c] - used[c]))

            candidate = build(new_left)

            if answer == "" or candidate < answer:
                answer = candidate

        return answer