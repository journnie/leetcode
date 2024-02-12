class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        attacks = len(timeSeries)
        poisoned = 0
        for i in range(attacks):
            if i < attacks-1 and timeSeries[i+1] - timeSeries[i] < duration:
                poisoned += timeSeries[i+1] - timeSeries[i]
            else:
                poisoned += duration

        return poisoned
                        