class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        shuffle_list = []
        x_list = nums[:n]
        y_list = nums[n:]
        for i in range(n):
            shuffle_list.append(x_list[i])
            shuffle_list.append(y_list[i])
        return shuffle_list