class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        # square matrix
        n = len(mat)
        diagonal_sum = 0

        for i in range(n):
            diagonal_sum += mat[i][i] + mat[i][n-i-1]
            if i == n-i-1:
                diagonal_sum -= mat[i][i]
        return diagonal_sum
