class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        # for m x n matrix
        m = len(matrix) # rows
        n = len(matrix[0]) # columns
        diag_bool = True

        # diagonals in horizontal
        for col in range(n):
            row = 0
            first_diagonal = matrix[row][col]
            while row < m and col < n:
                if matrix[row][col] != first_diagonal:
                    diag_bool = False
                row += 1
                col += 1
        # diagonals in vertical
        for row in range(m):
            col = 0
            first_diagonal = matrix[row][col]
            while row < m and col < n:
                if matrix[row][col] != first_diagonal:
                    diag_bool = False
                row += 1
                col += 1
        return diag_bool