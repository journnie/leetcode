class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        x_list = nums[:n]
        y_list = nums[n:]
        result_list = []

        for i in range(n) :
            x = x_list[i]
            y = y_list[i]
            result_list.append(x)
            result_list.append(y)

        return result_list