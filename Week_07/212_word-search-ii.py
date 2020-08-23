class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        WORD_KEY = '$'

        trie = {}
        # 插入到trie里面
        for word in words:
            node = trie
            for letter in word:
                # 如果字典中没有，就创建{}
                node = node.setdefault(letter,{})
            #结束符
            node[WORD_KEY] = word
        
        rowNum = len(board)
        colNum = len(board[0])

        matchWords = []

        # 循环
        def backtracking(row,col,parent):
            # 传进来parent是一个数组
            letter = board[row][col]
            # 该字母节点，包含下一个节点字典
            currNode = parent[letter]

            # 如果找到匹配的
            word_match = currNode.pop(WORD_KEY,False)
            if word_match:
                # 加入到结果集
                matchWords.append(word_match)
            # 比较已经访问过
            board[row][col] = '#'
            
            #四维遍历
            for (rowOffset,colOffset) in [(-1,0),(0,1),(1,0),(0,-1)]:
                newRow,newCol = row+rowOffset,col+colOffset
                # 判断没越界
                if newRow < 0 or newRow >= rowNum or newCol < 0 or newCol >= colNum:
                    continue
                if not board[newRow][newCol] in currNode:
                    continue
                backtracking(newRow,newCol,currNode)
            
            board[row][col] = letter
        
        for row in range(rowNum):
            for col in range(colNum):
                # 如果第一个字母在字典树中
                if board[row][col] in trie:
                    backtracking(row,col,trie)
        return matchWords