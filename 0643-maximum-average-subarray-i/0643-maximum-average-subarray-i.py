class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        current_sum = sum(nums[:k])
        max_sum = current_sum
        
        for i in range(len(nums)-k):
            current_sum += nums[i+k] - nums[i]
            if current_sum > max_sum:
                max_sum = current_sum

        return max_sum/k
        