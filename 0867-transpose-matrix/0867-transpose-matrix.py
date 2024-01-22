class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        transposed_matrix = []
        for j in range(len(matrix[0])):
            new_row = []
            for i in range(len(matrix)):
                new_row.append(matrix[i][j])
            transposed_matrix.append(new_row)
        return transposed_matrix
