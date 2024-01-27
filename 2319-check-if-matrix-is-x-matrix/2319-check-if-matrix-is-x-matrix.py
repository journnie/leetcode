class Solution:
    def checkXMatrix(self, grid: List[List[int]]) -> bool:
        for i in range(len(grid)):
            # check if the green part has zero
            if grid[i][i] == 0 or grid[i][len(grid)-1 - i] == 0:
                return False
            # if non-zeros, change them into zeros
            grid[i][i] = 0
            grid[i][len(grid) - 1 - i] = 0
            # check if the whole row is a list of zero
            if grid[i] != [0] * len(grid[0]):
                return False

        return True