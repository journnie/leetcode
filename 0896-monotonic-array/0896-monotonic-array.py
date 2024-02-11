class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        decreasing = True
        increasing = True

        for i in range(len(nums) - 1):
            if nums[i] > nums[i+1]:
                increasing = False
            if nums[i] < nums[i+1]:
                decreasing = False

            if not decreasing and not increasing:
                return False
        return True