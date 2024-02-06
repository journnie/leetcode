class Solution:
    def isWinner(self, player1: List[int], player2: List[int]) -> int:
        score1 = Solution.getScore(player1)
        score2 = Solution.getScore(player2)
        print(score1, score2)

        result = 0
        if score1 > score2:
            result = 1
        elif score1 < score2:
            result = 2

        return result

    @staticmethod
    def getScore(player):
        score = 0

        for i, hit in enumerate(player):
            # 2x if the player hit 10 pins in any of the previous two turns
            if i > 0 and player[i-1] == 10:
                score += 2 * hit
            elif i > 1 and player[i-2] == 10:
                score += 2 * hit
            # otherwise x
            else:
                score += hit

        return score
