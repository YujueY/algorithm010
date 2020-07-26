class Solution:
    def dfs(self, grid, r, c):
        grid[r][c] = "0"
        nr = len(grid)
        nl = len(grid[0])
        for x, y in [(r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)]:
            if 0 <= x < nr and 0 <= y < nl and grid[x][y] == "1":
                self.dfs(grid, x, y)

    def numIslands(self, grid: List[List[str]]) -> int:
        nr = len(grid)
        if nr == 0:
            return 0
        nl = len(grid[0])
        num_island = 0
        for r in range(nr):
            for l in range(nl):
                if grid[r][l] == "1":
                    num_island += 1
                    self.dfs(grid, r, l)
        return num_island
