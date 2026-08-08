class Solution:
    def hIndex(self, citations):
        n = len(citations)

        left = 0
        right = n - 1

        while left <= right:
            mid = (left + right) // 2

            # Number of papers from mid to the end
            papers = n - mid

            if citations[mid] >= papers:
                # This could be the answer,
                # try to find a larger H-index
                right = mid - 1
            else:
                # Not enough citations
                left = mid + 1

        return n - left