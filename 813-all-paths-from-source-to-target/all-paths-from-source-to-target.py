class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        ans = []
        path = [0]

        def dfs(node):
            # Reached target
            if node == len(graph) - 1:
                ans.append(path[:])
                return

            for nei in graph[node]:
                path.append(nei)

                dfs(nei)

                path.pop()

        dfs(0)

        return ans