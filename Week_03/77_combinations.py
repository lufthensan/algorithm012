from typing import List

class Solution:
    def combine(self,n:int,k:int):
        if n <= 0 or k <= 0 or k>n:
            return []

        res = []
        self.__dfs(1,k,n,[],res)
        return res

    def __dfs(self,start,k,n,pre,res):
        # 已经找到的组合存放在pre中，需要从start开始找元素
        # 在第k层结算
        if len(pre) == k:
            res.append(pre[:])
            return

        for i in range(start,n+1):
            pre.append(i)
            self.__dfs(i+1,k,n,pre,res)
            #回溯的时候，重置状态
            pre.pop()