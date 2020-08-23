class Solution:
    def minMutation(self,start,end,bank):
        possible = ["A","C","G","T"]
        queue = [(start,0)]
        while queue:
            (word,step)= queue.pop(0)
            if word == end:
                return step
            for i in range(len(word)):
                for p in possible:
                    # 从0位开始匹配
                    temp = word[:i] + p + word[i+1:]
                    # 判断是否在bank里面
                    if temp in bank:
                        bank.remove(temp)
                        queue.append((temp,step + 1))
        return -1