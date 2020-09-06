class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        res = []
        left = 0
        right = 0
        match = 0
        window = {}
        # 目标p变成map形式，记录出现次数
        needs = dict((i,p.count(i)) for i in p)

        while right < len(s):
            c1 = s[right]
            # 如果在目标字符串中
            if c1 in needs.keys():
                # 在窗口中新增
                window[c1] = window.get(c1,0)+1
                if window[c1] == needs[c1]:
                    # 表示已经有一个字符已经匹配完毕了
                    match += 1
            # 指针右移
            right += 1
            
            # 表明所有的字符都已经匹配完毕了
            while match == len(needs):
                # 如果等于目标，就表明是最小匹配串了，添加到res里面
                if right - left  == len(p):
                    res.append(left)
                c2 = s[left]
                #如果在匹配的字符中，就需要从windows的map中减去个数后判断
                if c2 in needs.keys():
                    window[c2] -= 1
                    #小于表明删除的是目标的字符
                    if window[c2] < needs[c2]:
                        match -= 1
                left += 1
        return res