class Solution:
    def fib(self, n: int) -> int:
        def fib2(n, memo={}):
            if n == 1:
                return 1
            elif n == 0:
                return 0
            elif n in memo:
                return memo[n]
            else:
                result = fib2(n-1,memo) + fib2(n-2,memo)
                memo[n] = result
                return result
        return fib2(n)
        