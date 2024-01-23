class Solution:
    def checkXMatrix(self, grid: List[List[int]]) -> bool:
         # n x n matrix
        n = len(grid)

        # check the diagonals != 0; True
        # primary diagonal elements
        row = 0
        col = 0
        while row < n:
            if grid[row][col] == 0:
                return False
            row += 1
            col += 1
        # secondary diagonal elements
        row = 0
        col = n - 1
        while row < n:
            if grid[row][col] == 0:
                return False
            row += 1
            col -= 1

        # check the non-diagonals == 0; True
        for i in range(n):
            for j in range(n):
                if i != j and j != n-1-i:
                    if grid[i][j] != 0:
                        return False
        return True