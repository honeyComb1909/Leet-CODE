import heapq

class Solution:
    def networkDelayTime(self, times, n, k):

        graph = [[] for _ in range(n + 1)]

        # Build graph
        for u, v, w in times:
            graph[u].append((v, w))

        # Distance from k to every node
        dist = [float('inf')] * (n + 1)
        dist[k] = 0

        # Min heap: (distance, node)
        heap = [(0, k)]

        while heap:
            time, node = heapq.heappop(heap)

            # Ignore outdated entry
            if time > dist[node]:
                continue

            for nei, weight in graph[node]:

                new_time = time + weight

                if new_time < dist[nei]:
                    dist[nei] = new_time
                    heapq.heappush(heap, (new_time, nei))

        # If any node is unreachable
        for i in range(1, n + 1):
            if dist[i] == float('inf'):
                return -1

        return max(dist[1:])