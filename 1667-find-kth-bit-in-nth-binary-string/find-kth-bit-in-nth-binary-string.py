class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        invert = False

        while n > 1:
            length = (1 << n) - 1
            mid = (length + 1) // 2

            if k == mid:
                return "0" if invert else "1"

            if k > mid:
                # Move to the corresponding position
                # in the left half and invert the bit.
                k = length - k + 1
                invert = not invert

            n -= 1

        # S1 = "0"
        return "1" if invert else "0"