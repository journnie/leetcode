class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        total_damage = 0
        trials = len(timeSeries)

        for i in range(trials) :
            if i < trials - 1 :
                if timeSeries[i+1] - timeSeries[i] >= duration:
                    total_damage += duration
                
                if timeSeries[i+1] - timeSeries[i] < duration:
                    total_damage += timeSeries[i+1] - timeSeries[i]
            
            else : # i == trials
                total_damage += duration

        return total_damage
            