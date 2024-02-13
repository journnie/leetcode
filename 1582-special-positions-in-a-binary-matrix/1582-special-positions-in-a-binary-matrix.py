class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        # m x n matrix
        m = len(mat)
        n = len(mat[0])

        location = []
        
        special = 0 

        rows = [0] * m
        cols = [0] * n

        for i in range(m):
            for j in range(n):
                if mat[i][j] == 1:
                    location.append([i, j])
                    rows[i] += 1
                    cols[j] += 1
                    
        for loc in location:
            x, y = loc
            if rows[x] == 1 and cols[y] == 1:
                special += 1
    
        return special