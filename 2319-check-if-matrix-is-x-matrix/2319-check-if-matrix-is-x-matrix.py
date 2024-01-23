class Solution:
    def checkXMatrix(self, grid: List[List[int]]) -> bool:
         # n x n matrix
        n = len(grid)
         # check the non-diagonals == 0; True
        for i in range(n):
            for j in range(n):
                if i == j or j == n-1-i:
                    if grid[i][j] == 0:
                        return False
                else:
                    if grid[i][j] != 0:
                        return False
        return True