class Solution:
    def licenseKeyFormatting(self, s, k):
        # Remove '-' and convert to uppercase
        s = s.replace("-", "").upper()

        if not s:
            return ""

        # First group size
        first = len(s) % k

        result = []

        if first:
            result.append(s[:first])

        # Remaining groups
        for i in range(first, len(s), k):
            result.append(s[i:i + k])

        return "-".join(result)