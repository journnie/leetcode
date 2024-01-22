class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        maxWealth = 0
        for account in accounts:
            newWealth = sum(account)
            if newWealth > maxWealth:
                maxWealth = newWealth
        return maxWealth
        