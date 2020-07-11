class Solution:
    def trap(self, height: List[int]) -> int:
        # 用三个下标，先遍历一遍数组，找出符合下面特性的数的序列以及值
        # 1.元素左右两边的值都比它低
        # 2.元素不能是数组头尾位置
        # 两两数组判断高低，低的覆盖中间的位置
        # 数组相加，与原数组相减，即为蓄水面积
        # columns = []
        # sum = 0
        # sum_rain = 0
        # for i in height:
        #     if i==0 or i==len(height)-1:
        #         sum += height[i]
        #         continue
        #     if height[i] > height[i-1] and height[i]>height[i+1]:
        #         sum += height[i]
        #         columns.insert(i,height[i])
        # for i in columns:
        #     rain_heigh=0
        #     if columns[i][1] > columns[i+1][1]:
        #         rain_heigh = columns[i+1][1]
        #     else:
        #         rain_heigh = columns[i][1]
        #     while j==column[i][0]+1 and j<columns[i+1][0]:
        #         height[j] = rain_heigh
        # for i in height:
        #     sum_rain += height[i]
        # return sum_rain-sum

        if not height: return 0
        n = len(height)

        left,right = 0,n-1
        max_left,max_right = height[left],height[right]
        ans=0

        while left <= right:
            max_left = max(height[left],max_left)
            max_right = max(height[right],max_right)
            if max_left < max_right:
                ans += max_left - height[left]
                left += 1
            else:
                ans += max_right - height[right]
                right -=1
        return ans
