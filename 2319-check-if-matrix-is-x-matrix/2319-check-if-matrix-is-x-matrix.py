class Solution:
    def checkXMatrix(self, grid: List[List[int]]) -> bool:
        # n x n matrix
        n = len(grid)

        for i in range(n):
            if grid[i][i] == 0 or grid[i][n-i-1] == 0:
                return False
            grid[i][i] = grid[i][n - i - 1] = 0

        for i in range(n):
            if sum(grid[i]) != 0:
                return False

        return True
