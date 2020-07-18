"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        # 如果是空的，就直接返回
        if root is None:
            return []

        #先把root压入栈
        stack = [root,]
        result = []
        while stack:
            root = stack.pop()
            if root is not None:
                # 看解析就类似于先root，后v1,v2,v3
                result.append(root.val);
            # 吧子压入栈
            for c in root.children:
                stack.append(c)
        return result[::-1]