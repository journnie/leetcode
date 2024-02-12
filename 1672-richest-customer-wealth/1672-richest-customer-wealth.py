class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        richest = 0
        for rich in accounts:
            wealth = sum(rich)
            if wealth > richest:
                richest = wealth
        return richest
