class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        # check if the diagonally below element is the same
        for i in range(len(matrix) - 1):
            for j in range(len(matrix[0]) - 1):
                number = matrix[i][j]
                if number != matrix[i + 1][j + 1]:
                    return False
        return True