class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        list = []
        x = nums[:n]
        y = nums[n:]
        for i, j in zip(x, y):
            list += [i, j]
        return list