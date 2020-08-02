class Solution:
    def isPerfectSquare(self, num):
        left = 0
        right = num // 2 + 1
        while left < right:
            mid = (left + right + 1) >> 1
            square = mid * mid
            if square > num:
                right = mid - 1
            elif square < num:
                left = mid
            else:
                return True
        return False