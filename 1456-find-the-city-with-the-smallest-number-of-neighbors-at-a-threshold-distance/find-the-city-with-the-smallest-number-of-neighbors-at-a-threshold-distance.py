import heapq

class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:

        graph = [[] for _ in range(n)]

        # Build undirected graph
        for u, v, w in edges:
            graph[u].append((v, w))
            graph[v].append((u, w))

        answer = -1
        min_count = float('inf')

        for start in range(n):

            dist = [float('inf')] * n
            dist[start] = 0

            heap = [(0, start)]

            while heap:
                d, node = heapq.heappop(heap)

                if d > dist[node]:
                    continue

                # No need to explore paths beyond threshold
                if d > distanceThreshold:
                    continue

                for nei, weight in graph[node]:

                    new_dist = d + weight

                    if new_dist <= distanceThreshold and new_dist < dist[nei]:
                        dist[nei] = new_dist
                        heapq.heappush(heap, (new_dist, nei))

            # Count reachable cities
            count = 0

            for i in range(n):
                if i != start and dist[i] <= distanceThreshold:
                    count += 1

            # Need larger index in case of tie
            if count <= min_count:
                min_count = count
                answer = start

        return answer