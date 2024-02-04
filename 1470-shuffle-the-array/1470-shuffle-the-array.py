class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        shuffle_arr = []
        for i in range(n):
            shuffle_arr.append(nums[i])
            shuffle_arr.append(nums[n + i])

        return shuffle_arr