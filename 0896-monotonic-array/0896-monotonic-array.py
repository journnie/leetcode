class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        monotonic = 0
        for i in range(len(nums)-1):
            if nums[i] > nums[i+1]:
                if monotonic == 1:
                    return False
                monotonic = -1
            elif nums[i] < nums[i+1]:
                if monotonic == -1:
                    return False
                monotonic = 1
            else:
                continue
        return True