import heapq

class Solution:
    def kSmallestPairs(self, nums1, nums2, k):
        heap = []
        result = []

        # Put the first pair for each nums1 element
        for i in range(min(k, len(nums1))):
            heapq.heappush(heap, (nums1[i] + nums2[0], i, 0))

        while heap and len(result) < k:
            total, i, j = heapq.heappop(heap)

            result.append([nums1[i], nums2[j]])

            # Move to the next element in nums2
            if j + 1 < len(nums2):
                heapq.heappush(
                    heap,
                    (nums1[i] + nums2[j + 1], i, j + 1)
                )

        return result