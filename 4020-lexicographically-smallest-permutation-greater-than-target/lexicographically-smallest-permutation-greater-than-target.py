class Solution:
    def lexGreaterPermutation(self, s: str, target: str) -> str:
        cnt = [0] * 26
        for c in s:
            cnt[ord(c) - 97] += 1

        n = len(target)

        def build(prefix, pos):
            res = prefix[:]
            c = cnt[:]
            for i in range(pos, n):
                ch = target[i]
                idx = ord(ch) - 97
                if c[idx]:
                    c[idx] -= 1
                    res += ch
                else:
                    return None
            return res

        # Try to keep target's prefix as long as possible.
        ans = None

        for i in range(n - 1, -1, -1):
            used = [0] * 26
            possible = True

            for j in range(i):
                x = ord(target[j]) - 97
                used[x] += 1
                if used[x] > cnt[x]:
                    possible = False
                    break

            if not possible:
                continue

            # At position i, choose the smallest character > target[i].
            t = ord(target[i]) - 97
            for x in range(t + 1, 26):
                if cnt[x] > used[x]:
                    rem = cnt[:]
                    for k in range(26):
                        rem[k] -= used[k]
                    rem[x] -= 1

                    suffix = []
                    for k in range(26):
                        suffix.append(chr(k + 97) * rem[k])

                    candidate = target[:i] + chr(x + 97) + ''.join(suffix)
                    if ans is None or candidate < ans:
                        ans = candidate
                    break

            if ans is not None:
                return ans

        return ""