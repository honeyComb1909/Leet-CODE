import heapq

class Graph:

    def __init__(self, n: int, edges: List[List[int]]):
        self.graph = [[] for _ in range(n)]

        for u, v, w in edges:
            self.graph[u].append((v, w))

    def addEdge(self, edge: List[int]) -> None:
        u, v, w = edge

        self.graph[u].append((v, w))

    def shortestPath(self, node1: int, node2: int) -> int:

        n = len(self.graph)

        dist = [float('inf')] * n
        dist[node1] = 0

        heap = [(0, node1)]

        while heap:
            d, node = heapq.heappop(heap)

            if d > dist[node]:
                continue

            if node == node2:
                return d

            for nei, weight in self.graph[node]:

                new_dist = d + weight

                if new_dist < dist[nei]:
                    dist[nei] = new_dist
                    heapq.heappush(heap, (new_dist, nei))

        return -1