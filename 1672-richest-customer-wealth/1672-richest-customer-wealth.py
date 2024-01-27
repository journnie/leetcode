class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        customers = len(accounts)
        money = []

        for customer in range(customers):
            money.append(sum(accounts[customer]))

        return max(money)

