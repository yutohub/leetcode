class Solution(object):
    def numIslands(self, grid):
        if grid is None or len(grid) == 0:
            return 0
        
        islands = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == '1':
                    self.explore(grid, i, j)
                    # Count when exploration is complete.
                    islands += 1
        return islands

    def explore(self, grid, i, j):
        grid[i][j] = 'X'
        # Top
        if i - 1 >= 0 and grid[i - 1][j] == '1':
            self.explore(grid, i - 1, j)
        # Left
        if j - 1 >= 0 and grid[i][j - 1] == '1':
            self.explore(grid, i, j - 1)
        # Bottom
        if i + 1 < len(grid) and grid[i + 1][j] == '1':
            self.explore(grid, i + 1, j)
        # Right
        if j + 1 < len(grid[i]) and grid[i][j + 1] == '1':
            self.explore(grid, i, j + 1)
        