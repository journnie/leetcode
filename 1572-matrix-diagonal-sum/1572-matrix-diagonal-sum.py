class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        n = len(mat)
        primary_sum = 0
        secondary_sum = 0
        for i in range(n):
            primary_sum += mat[i][i]

        for j in range(n):
            print(j, n - 1 -j)
            secondary_sum += mat[j][n - 1 -j]
        if n % 2 != 0:
            mid = n//2
            overlap = mat[mid][mid]
        else:
            overlap = 0
        return primary_sum + secondary_sum - overlap