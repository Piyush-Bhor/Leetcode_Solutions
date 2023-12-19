class Solution(object):
    def tribonacci(self, n):
        """
        :type n: int
        :rtype: int
        """
        def trib(n,memo={}):
            if n == 0:
                return 0
            elif n == 1 or n == 2:
                return 1
            elif n in memo:
                return memo[n]
            else:
                result = trib(n-1,memo) + trib(n-2,memo) + trib(n-3,memo)
                memo[n] = result
                return result
        return(trib(n))
        