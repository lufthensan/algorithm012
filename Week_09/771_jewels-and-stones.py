class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        J_set = set(J)
        return sum(ston in J_set for ston in S)