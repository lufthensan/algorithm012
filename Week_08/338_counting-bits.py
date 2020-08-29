class Solution:
    def countBits(self, num: int) -> List[int]:
        ans = [i for i in range(num+1)]
        for i in range(len(ans)):
            if ans[i] & 1 == 1:
                # 如果是奇数
                ans[i] = ans[i-1] + 1
            else:
                # 偶数
                ans[i] = ans[i//2]
        return ans 
        