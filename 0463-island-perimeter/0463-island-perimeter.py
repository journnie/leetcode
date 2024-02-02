class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        # grid
        rows = len(grid)
        cols = len(grid[0])

        perimeter = 0

        for x in range(rows):
            for y in range(cols):
                if grid[x][y] == 1:

                    perimeter += 4

                    # if the land has adjusted land
                    if x > 0 and grid[x-1][y] == 1:
                        perimeter -= 1
                    if x < rows-1 and grid[x+1][y] == 1:
                        perimeter -= 1
                    if y > 0 and grid[x][y-1] == 1:
                        perimeter -= 1
                    if y < cols-1 and grid[x][y+1] == 1:
                        perimeter -= 1

        return perimeter