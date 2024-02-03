class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        if n == 1:
            return [[i] for i in nums]

        permutations = []

        for idx, val in enumerate(nums):
            rest_per = self.permute(nums[:idx] + nums[idx+1:])
            
            for perm in rest_per:
                permutations.append([val] + perm)

        return permutations
