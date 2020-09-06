class Solution:
    def myAtoi(self, str: str) -> int:
        str = str.strip()
        if not str: return 0
        res,i,sign = 0,1,1
        int_max,int_min,boundry = 2**31-1 ,-2**31,2**31 //10
        if str[0] == '-':sign = -1  #保存负号
        # 若无负号为，则需从i=0开始数字拼接
        elif str[0] != '+': i=0
        for c in str[i:]:
            # 遇到非数字跳出
            if not '0' <= c <= '9': break
            if res > boundry or res == boundry and c > '7':
                return int_max if sign==1 else int_min
            res = 10*res + ord(c)-ord('0')  #数字拼接
        return sign * res