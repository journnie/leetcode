class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        k = len(nums)
        num_set = set(nums)
        all_set = set(range(1, k+1))

        disappeared_nums = list(all_set - num_set)

        return disappeared_nums