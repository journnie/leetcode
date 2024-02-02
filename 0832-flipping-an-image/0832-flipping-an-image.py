class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        n = len(image)
        new_image = [[0 for i in range(n)] for j in range(n)]

        for i in range(n):
            for j in range(n):
                if image[i][j] == 0:
                    new_image[i][n - j - 1] = 1
                else:
                    new_image[i][n - j - 1] = 0

        return new_image