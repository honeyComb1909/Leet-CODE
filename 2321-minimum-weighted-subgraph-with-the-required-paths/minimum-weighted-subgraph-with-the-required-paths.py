import heapq

class Solution:
    def minimumWeight(self, n, edges, src1, src2, dest):

        graph = [[] for _ in range(n)]
        reverse_graph = [[] for _ in range(n)]

        for u, v, w in edges:
            graph[u].append((v, w))
            reverse_graph[v].append((u, w))

        def dijkstra(start, graph):
            dist = [float('inf')] * n
            dist[start] = 0

            heap = [(0, start)]

            while heap:
                d, node = heapq.heappop(heap)

                if d > dist[node]:
                    continue

                for nei, weight in graph[node]:
                    new_dist = d + weight

                    if new_dist < dist[nei]:
                        dist[nei] = new_dist
                        heapq.heappush(heap, (new_dist, nei))

            return dist

        # Distance from src1 to every node
        d1 = dijkstra(src1, graph)

        # Distance from src2 to every node
        d2 = dijkstra(src2, graph)

        # Distance from every node to dest
        d3 = dijkstra(dest, reverse_graph)

        answer = float('inf')

        for i in range(n):

            if d1[i] == float('inf'):
                continue

            if d2[i] == float('inf'):
                continue

            if d3[i] == float('inf'):
                continue

            total = d1[i] + d2[i] + d3[i]

            answer = min(answer, total)

        return -1 if answer == float('inf') else answer