class Solution:
    def validPath(self, n: int, edges: List[List[int]],
                  source: int, destination: int) -> bool:

        graph = [[] for _ in range(n)]

        # Build adjacency list
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        visited = [False] * n
        queue = [source]
        visited[source] = True

        front = 0

        while front < len(queue):
            node = queue[front]
            front += 1

            if node == destination:
                return True

            for nei in graph[node]:
                if not visited[nei]:
                    visited[nei] = True
                    queue.append(nei)

        return False