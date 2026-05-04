class Solution:
    def climbStairs(self, n: int) -> int:
        memo = {}
        def stairs(n):
            if n == 0:
                return 1
            if n < 0:
                return 0
            if n in memo:
                return memo[n]
            memo[n] = stairs(n-1) + stairs(n-2)
            return memo[n] 
        return stairs(n)