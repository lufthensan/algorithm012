class Solution:
    def reverseOnlyLetters(self, S: str) -> str:
        ans = []
        # j从最后一个下标开始计算
        j = len(S)-1

        for i,x in enumerate(S):
            if x.isalpha():
                
                while not S[j].isalpha():
                    j -=1
                
                ans.append(S[j])
                j -=1
            
            else:
                ans.append(x)
        return "".join(ans)