from collections import defaultdict
from bisect import bisect_left, bisect_right


class RangeFreqQuery:

    def __init__(self, arr: list[int]):
        self.positions = defaultdict(list)

        # Store indices for every value
        for i, value in enumerate(arr):
            self.positions[value].append(i)

    def query(self, left: int, right: int, value: int) -> int:

        if value not in self.positions:
            return 0

        indices = self.positions[value]

        # First index >= left
        start = bisect_left(indices, left)

        # First index > right
        end = bisect_right(indices, right)

        return end - start