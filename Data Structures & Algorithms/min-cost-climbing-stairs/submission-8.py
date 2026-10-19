class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        memo = [0] * (len(cost) + 1)
        memo[0] = 0
        memo[1] = 0
        if len(cost) == 2:
            return min(cost[0], cost[1])

        for c in range(2, len(cost) +1):
            memo[c] = min(memo[c-1] + cost[c-1], memo[c-2] + cost[c-2])

        return memo[len(cost)]
