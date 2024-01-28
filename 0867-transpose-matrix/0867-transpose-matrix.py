class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        # m x n matrix
        m = len(matrix)
        n = len(matrix[0])

        transposed_matrix = [] # n x m

        for j in range(n):
            transposed_row = []
            for i in range(m):
                transposed_row.append(matrix[i][j])
            transposed_matrix.append(transposed_row)

        return transposed_matrix
