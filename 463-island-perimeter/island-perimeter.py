class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])

        visited = set()

        def dfs(r, c):
            # Outside grid = perimeter
            if r < 0 or r >= rows or c < 0 or c >= cols:
                return 1

            # Water = perimeter
            if grid[r][c] == 0:
                return 1

            # Already visited land
            if (r, c) in visited:
                return 0

            visited.add((r, c))

            perimeter = 0

            perimeter += dfs(r + 1, c)
            perimeter += dfs(r - 1, c)
            perimeter += dfs(r, c + 1)
            perimeter += dfs(r, c - 1)

            return perimeter

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    return dfs(r, c)

        return 0