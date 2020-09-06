class Solution:
    def reverseWords(self, s: str) -> str:
        # 先全部反转
        s = s[::-1]
        s = s.split(" ")
        s.reverse()
        return " ".join(s)