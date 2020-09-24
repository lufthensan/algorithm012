class Solution:
    def canJump(self, nums):
        max_i = 0  # 初始化当前能到达最远的位置
        for i, jump in enumerate(nums):  # i 为当前位置，jump是当前位置的跳数
            if max_i >= i and i + jump > max_i:  # 如果当前位置能到达，并且当前位置+跳数>最远位置
                max_i = i + jump
        return max_i >= i # 此时i指向最远