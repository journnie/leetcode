class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        n = len(nums)
        num_set = set(nums)
        missing_num = []

        for i in range(1, n + 1):
            if i not in num_set:
                missing_num.append(i)

        return missing_num