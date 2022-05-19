class Solution:
    def maxAreaOfIsland(self, grid):
        if grid is None or len(grid) == 0:
            return 0

        max_area = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 1:
                    area = 0
                    area = self.explore(grid, i, j, area)
                    if area > max_area:
                        max_area = area
        return max_area
                    
    def explore(self, grid, i, j, area):
        grid[i][j] = 'X'
        area += 1
        # up
        if i - 1 >= 0 and grid[i - 1][j] == 1:
            area = self.explore(grid, i - 1, j, area)
        # left
        if j - 1 >= 0 and grid[i][j - 1] == 1:
            area = self.explore(grid, i, j - 1, area)
        # down
        if i + 1 < len(grid) and grid[i + 1][j] == 1:
            area = self.explore(grid, i + 1, j, area)
        # right
        if j + 1 < len(grid[i]) and grid[i][j + 1] == 1:
            area =self.explore(grid, i, j + 1, area)
        return area
        