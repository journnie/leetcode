class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        # m x n matrix
        m = len(mat)
        n = len(mat[0])

        numbers = []
        reshaped_mat = [[0 for i in range(c)] for j in range(r)]

        # the reshape operation with given parameters is not possible
        if m * n != r * c:
            return mat  # output the original matrix.
        
        for row in mat:
            for element in row:
                numbers.append(element)

        for i in range(r):
            for j in range(c):
                reshaped_mat[i][j] = numbers[(c * i) + j]
                
        return reshaped_mat