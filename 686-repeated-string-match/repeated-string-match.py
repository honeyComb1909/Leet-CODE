class Solution:
    def repeatedStringMatch(self, a, b):
        repeated = ""
        count = 0

        while len(repeated) < len(b):
            repeated += a
            count += 1

        if b in repeated:
            return count

        repeated += a
        count += 1

        if b in repeated:
            return count

        return -1