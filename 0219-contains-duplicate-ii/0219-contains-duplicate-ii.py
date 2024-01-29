class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        num_dict = {}
        for idx, num in enumerate(nums):
            if num not in num_dict:
                num_dict[num] = idx
            else: # num in num_dict
                if abs(idx - num_dict[num]) <= k:
                    return True
                num_dict[num] = idx
        return False