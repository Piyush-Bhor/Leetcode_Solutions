class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        def stairs(n,memo={}):
            if n == 1:
                return 1
            elif n == 2:
                return 2
            elif n in memo:
                return memo[n]
            else:
                result = stairs(n-2,memo) + stairs(n-1,memo)
                memo[n] = result
                return result
        return stairs(n)