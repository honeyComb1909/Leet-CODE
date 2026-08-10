class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        ans = []

        def backtrack(start, parts):
            # If we have 4 parts
            if len(parts) == 4:
                if start == len(s):
                    ans.append(".".join(parts))
                return

            # Each IP part can have at most 3 digits
            for end in range(start + 1, min(start + 4, len(s) + 1)):
                part = s[start:end]

                # Leading zero is not allowed: "01", "00"
                if len(part) > 1 and part[0] == '0':
                    continue

                # Valid range
                if int(part) > 255:
                    continue

                parts.append(part)
                backtrack(end, parts)
                parts.pop()

        backtrack(0, [])
        return ans