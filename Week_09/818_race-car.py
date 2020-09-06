class Solution:
    def racecar(self, target: int) -> int:
        # 类似斐波那契，初始化头几个位置需要的最短路径，后面的就先初始化为正无穷
        dp = [0,1,4]+[float('inf')]*target
        for t in range(3,target + 1):
            # 根据二进制位数推算出如果一直加速，是2的几次方
            # 如果一直加速，第n次的位置会是(2^n)-1
            # 如果目标位置刚好落在(2^n)-1上，就直接返回n
            k = t.bit_length()
            if t == 2**k-1:
                dp[t] = k
                continue
            for j in range(k-1):
                # 如果在到达目标之前往回走过一次的情况，那么剩下的举例就是t-((2^(k-1)-1)+(2^j-1)
                # 两个-1抵消掉，所以剩下的举例所需要的步数就是dp[t-2^(k-1)+2^j]
                # 同时要加上操作步数，走到这一步需要 (k-1)+j+2 ,2是两步调头
                dp[t] = min(dp[t],dp[t-2**(k-1)+2**j]+k-1+j+2)
            # 走了k次就是超过目标位置了，先超过目标位置，后调头的情况
            # 在第一次超过目标的时候就调头，所以不可能超过2target的举例
            if 2**k-1 - t <t:
                # 先加速k次，然后调头1次，所以是k+1次操作
                dp[t] = min(dp[t],dp[2**k-1-t]+k+1)
        return dp[target]