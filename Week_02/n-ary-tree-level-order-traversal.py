"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if root is None:
            return []
 
        result = []
        previous_layer = [root]
    
        while previous_layer:
            #新的一层
            result.append([])
            #下一层的栈
            next_layer = []
            # 遍历当前层的root
            for node in previous_layer:
                result[-1].append(node.val)
                next_layer.extend(node.children)
            previous_layer = next_layer
        return result