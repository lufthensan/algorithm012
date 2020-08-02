import collections

class Solution:
    def largestValues(self,root):
        queue = collections.deque
        result = []
        if not root:
            return result

        queue.append(root)
        while queue :
            net = []
            result.append(float('-inf'))
            for node in queue:
                result[-1] = max(result[-1],node.val)
                if node.left:
                    net.append(node.left)
                if node.right:
                    net.append(node.right)
            queue = net
        return result