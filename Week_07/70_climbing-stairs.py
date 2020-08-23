class Solution:
    def climbStairs(self, n: int) -> int:
        if n < 3:
            return n
        res = [0 for i in range(n)]
        res[0],res[1] = 1,2
        for i in range(2,n):
            res[i] = res[i-1] + res[i-2]
        return res[n-1]