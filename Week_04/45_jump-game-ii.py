class Solution:
    def jump(self, nums):
        end = 0
        maxPosition = 0
        steps = 0
        for i in range(len(nums)-1):
            maxPosition = max(maxPosition,i + nums[i])
            if i == end:    # 遇到边界，就更新边界，且步数+1
                end = maxPosition
                steps += 1
        return steps
