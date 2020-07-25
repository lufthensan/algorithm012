from typing import List

class Solution:
    def subsets(self,nums:List[int]) -> List[List[int]]:
        res = []
        n = len(nums)

        def helper(i,temp):
            res.append(temp)
            for j in range(i,n):
                helper(j+1,temp+[nums[j]])
        helper(0,[])
        return res