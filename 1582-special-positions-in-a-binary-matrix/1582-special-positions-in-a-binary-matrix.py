class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
         # m x n matrix
        m = len(mat)
        n = len(mat[0])
        special_count = 0


        for i in range(m):
            for j in range(n):
                special_bool = True

                # find the elements of 1
                if mat[i][j] == 1:
                    # check if it's special
                    for row in range(m):
                        if row != i:
                            if mat[row][j] != 0:
                                special_bool = False
                    for col in range(n):
                        if col != j:
                            if mat[i][col] != 0:
                                special_bool = False
                else:
                    special_bool = False
                if special_bool == True:
                    special_count += 1

        return special_count    