class Solution(object):
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        cost.append(0) 
        def stairs(n,memo={}):
            if n == 1:
                return cost[1]
            elif n == 0:
                return cost[0]
            elif n in memo:
                return memo[n]
            else:
                result = min(stairs(n-1,memo),stairs(n-2,memo)) + cost[n]
                memo[n] = result
                return result
        return stairs(len(cost)-1)