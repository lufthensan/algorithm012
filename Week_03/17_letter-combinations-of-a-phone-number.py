class Solution:
    def letterCombinations(self,digits):
        # 如果输入的是空的，就返回空
        if not digits:
            return []

        #映射表
        d = [" ","*","abc","def","ghi","jkl","mno","pqrs","tuv","wxyz"]
        res = []

        #递归
        def dfs(tmp,index):
            #index记录每次遍历到字符串的位置
            if index ==len(digits):
                res.append(tmp)
                return
            c = digits[index]
            # ord(c)-48是获取c的ASCII码然后-48,48是0的ASCII码
            # 比如c=2,2-0 从d列表获取下标为2，即abc
            letters = d[ord(c)-48]

            # 遍历字符串
            for i in letters:
                dfs(tmp+i,index+1)
        dfs("",0)
        return res