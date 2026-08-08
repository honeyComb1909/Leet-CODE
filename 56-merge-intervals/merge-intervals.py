class Solution:
    def merge(self, intervals):
        intervals.sort(key=lambda x: x[0])

        result = []

        for interval in intervals:
            start, end = interval

            # No overlap
            if not result or start > result[-1][1]:
                result.append([start, end])

            # Overlap
            else:
                result[-1][1] = max(result[-1][1], end)

        return result