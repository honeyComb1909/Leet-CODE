class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        graph = [[] for _ in range(n + 1)]

        for u, v, weight in roads:
            graph[u].append((v, weight))
            graph[v].append((u, weight))

        visited = [False] * (n + 1)
        queue = [1]
        visited[1] = True

        ans = float('inf')
        front = 0

        while front < len(queue):
            city = queue[front]
            front += 1

            for nei, weight in graph[city]:
                # Every edge in city 1's component
                # can affect the minimum score.
                ans = min(ans, weight)

                if not visited[nei]:
                    visited[nei] = True
                    queue.append(nei)

        return ans