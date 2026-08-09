from sortedcontainers import SortedList


class SummaryRanges:

    def __init__(self):
        self.values = SortedList()

    def addNum(self, value: int) -> None:
        if value not in self.values:
            self.values.add(value)

    def getIntervals(self) -> list[list[int]]:

        if not self.values:
            return []

        intervals = []

        left = self.values[0]
        right = self.values[0]

        for value in self.values[1:]:

            if value == right + 1:
                # Continue current interval
                right = value
            else:
                # Start a new interval
                intervals.append([left, right])
                left = value
                right = value

        # Add the final interval
        intervals.append([left, right])

        return intervals