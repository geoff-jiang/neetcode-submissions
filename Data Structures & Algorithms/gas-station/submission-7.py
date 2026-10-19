class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        
        n = len(gas)

        start = n - 1
        end = 0
        totalGas = (gas[start] - cost[start])
        while start > end:
            if totalGas >= 0:
                totalGas += gas[end] - cost[end]
                end += 1
            else:
                start -= 1
                totalGas += gas[start] - cost[start]
        
        return start if totalGas >= 0 else -1
            
