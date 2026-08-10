class Solution:
    def isPossible(self, n: int, edges: List[List[int]]) -> bool:
        graph = [set() for _ in range(n + 1)]

        for u, v in edges:
            graph[u].add(v)
            graph[v].add(u)

        odd = []

        for i in range(1, n + 1):
            if len(graph[i]) % 2 == 1:
                odd.append(i)

        # Already all even
        if len(odd) == 0:
            return True

        # More than 4 odd nodes cannot be fixed with 2 edges
        if len(odd) > 4:
            return False

        # Exactly 2 odd nodes
        if len(odd) == 2:
            a, b = odd

            # Add edge a-b
            if b not in graph[a]:
                return True

            # Try an intermediate node
            for c in range(1, n + 1):
                if c != a and c != b:
                    if c not in graph[a] and c not in graph[b]:
                        return True

            return False

        # Exactly 4 odd nodes
        a, b, c, d = odd

        def can_connect(x, y):
            return y not in graph[x]

        # (a,b) and (c,d)
        if can_connect(a, b) and can_connect(c, d):
            return True

        # (a,c) and (b,d)
        if can_connect(a, c) and can_connect(b, d):
            return True

        # (a,d) and (b,c)
        if can_connect(a, d) and can_connect(b, c):
            return True

        return False