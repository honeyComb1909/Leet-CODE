from collections import deque

class Solution:
    def shortestAlternatingPaths(
        self,
        n: int,
        redEdges: List[List[int]],
        blueEdges: List[List[int]]
    ) -> List[int]:

        # graph[node][color]
        # color 0 = red
        # color 1 = blue
        graph = [[[], []] for _ in range(n)]

        for u, v in redEdges:
            graph[u][0].append(v)

        for u, v in blueEdges:
            graph[u][1].append(v)

        # dist[node][color]
        # shortest distance to node when the last edge
        # used has this color
        dist = [[float('inf'), float('inf')] for _ in range(n)]

        # Start from node 0.
        # We allow either color as the "previous" color.
        dist[0][0] = 0
        dist[0][1] = 0

        queue = deque()

        queue.append((0, 0))
        queue.append((0, 1))

        while queue:
            node, last_color = queue.popleft()

            # Next edge must have opposite color
            next_color = 1 - last_color

            for nei in graph[node][next_color]:

                if dist[nei][next_color] == float('inf'):
                    dist[nei][next_color] = dist[node][last_color] + 1
                    queue.append((nei, next_color))

        ans = []

        for i in range(n):
            best = min(dist[i][0], dist[i][1])

            if best == float('inf'):
                ans.append(-1)
            else:
                ans.append(best)

        return ans