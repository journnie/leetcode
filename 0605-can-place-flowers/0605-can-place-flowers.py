class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        # if no flower to plant - True
        if n == 0: return True

        flowerbed_len = len(flowerbed)

        for i in range(flowerbed_len):
            # if already planted - pass
            if flowerbed[i] == 1:
                continue

            # checking if there is any adjacent flower
            # previous plot - index 0 has no previous plot
            if i != 0 and flowerbed[i-1] == 1:
                continue

            # next plot
            if i != flowerbed_len - 1 and flowerbed[i+1] == 1:
                continue

            # planting available
            flowerbed[i] = 1

            # reduce given flower
            n -= 1

            # no more flower to plant
            if n == 0:
                return True

        return False