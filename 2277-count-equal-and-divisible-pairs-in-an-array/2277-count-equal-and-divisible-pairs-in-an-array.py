class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
        count = 0
        for i, a in enumerate(nums):
            for j, b in enumerate(nums):
                if a != b or i <= j:
                    continue
                # a == b
                if (i * j) % k == 0:
                    count += 1

        return count