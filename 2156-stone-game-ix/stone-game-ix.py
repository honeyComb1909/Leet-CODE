class Solution:
    def stoneGameIX(self, stones: list[int]) -> bool:
        c0 = c1 = c2 = 0
        for x in stones:
            rem = x % 3
            if rem == 0:
                c0 += 1
            elif rem == 1:
                c1 += 1
            else:
                c2 += 1

        # If 0-stones are even, 0s cancel out in turn order.
        # Alice wins if both 1-stones and 2-stones exist.
        if c0 % 2 == 0:
            return c1 >= 1 and c2 >= 1

        # If 0-stones are odd, 0s flip who gets trapped.
        # Alice wins only if the difference between 1-stones and 2-stones is strictly greater than 2.
        return abs(c1 - c2) > 2