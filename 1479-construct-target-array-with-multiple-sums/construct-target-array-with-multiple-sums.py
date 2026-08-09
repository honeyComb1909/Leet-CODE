import heapq

class Solution:
    def isPossible(self, target):
        total = sum(target)

        # Max heap using negative values
        heap = [-x for x in target]
        heapq.heapify(heap)

        while True:
            largest = -heapq.heappop(heap)

            # All values are 1
            if largest == 1:
                return True

            rest = total - largest

            # Cannot reduce largest
            if rest == 0 or largest <= rest:
                return False

            # If rest == 1, largest can always be reduced to 1
            if rest == 1:
                return True

            previous = largest % rest

            # Cannot make a positive previous value
            if previous == 0:
                return False

            total = rest + previous
            heapq.heappush(heap, -previous)