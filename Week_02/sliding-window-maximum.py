class Solution:
    # def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
    #     n = len(nums)

    #     if n*k ==0:
    #         return []
    #     return [max(nums[i:i + k]) for i in range(n - k + 1)]


    # 分治算法
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        if n*k == 0:
            return []
        if k ==1:
            return nums

        # 建立Left数组
        left = [0] * n
        left[0] = nums[0]
        right = [0] * n
        right[n-1] = nums[n-1]
        for i in range(1,n):
            # 填充left
            if i % k ==0:
                #能整除表示是新块的第一个
                left[i] = nums[i]
            else:
                left[i] = max(left[i-1],nums[i])
            #填充right,方向从右往左
            j = n - i -1
            if (j+1) % k == 0:
                right[j] = nums[j]
            else:
                right[j] = max(right[j+1],nums[j])
        output = []
        for i in range(n-k+1):
            output.append(max(left[i+k-1],right[i]))

        return output