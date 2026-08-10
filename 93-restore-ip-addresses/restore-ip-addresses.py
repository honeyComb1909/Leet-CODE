class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        ans = []
        path = []

        def backtrack(start):
            # If we have 4 parts
            if len(path) == 4:
                if start == len(s):
                    ans.append(".".join(path))
                return

            # Each IP part can have length 1, 2, or 3
            for length in range(1, 4):
                if start + length > len(s):
                    break

                part = s[start:start + length]

                # Leading zero is invalid: "01", "00"
                if len(part) > 1 and part[0] == '0':
                    continue

                # Must be <= 255
                if int(part) > 255:
                    continue

                path.append(part)
                backtrack(start + length)
                path.pop()

        backtrack(0)
        return ans