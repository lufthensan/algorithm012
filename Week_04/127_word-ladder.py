from collections import defaultdict


class Solution:

    def __init__(self):
        self.length = 0
        self.all_comobo_dict = defaultdict(list)

    def visitWordNode(self, queue, visited, others_visited):
        current_word, level = queue.pop(0)
        for i in range(self.length):
            # 通用状态
            intermidiate_word = current_word[:i] + '*' + current_word[i + 1:]

            # 根据通用状态找有几个单词有关联
            for word in self.all_comobo_dict[intermidiate_word]:
                # 如果另一条路已经访问过了，等于链路已经通了
                if word in others_visited:
                    return level + others_visited[word]
                # 表示还没会面，加入到自己的访问列表中去
                if word not in visited:
                    visited[word] = level + 1
                    queue.append((word, level + 1))
        return None

    def ladderLength(self, beginWord, endWord, wordList):
        if endWord not in wordList or not endWord or not beginWord or not wordList:
            return 0

        # wordList长度一致
        self.length = len(beginWord)

        for word in wordList:
            for i in range(self.length):
                # 通用状态，比如key = *ey k*y ke* 做成一个字典
                self.all_combo_dict[word[:i] + '*' + word[i + 1:]].append(word)

        # 两个起点
        queue_begin = [(beginWord, 1)]
        queue_end = [(endWord, 1)]

        visited_begin = {beginWord, 1}
        visited_end = {endWord, 1}
        ans = None

        while queue_begin and queue_end:
            ans = self.visitWordNode(queue_begin,visited_begin,visited_end)
            if ans:
                return ans

            #从endWord开始推
            ans = self.visitWordNode(queue_end,visited_end,visited_begin)
            if ans:
                return ans
        return 0
