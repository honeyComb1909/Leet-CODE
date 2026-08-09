import heapq

class Solution:
    def lastStoneWeight(self, stones):
        # Convert to max heap using negative values
        stones = [-x for x in stones]
        heapq.heapify(stones)

        while len(stones) > 1:
            a = -heapq.heappop(stones)
            b = -heapq.heappop(stones)

            if a != b:
                heapq.heappush(stones, -(a - b))

        return -stones[0] if stones else 0