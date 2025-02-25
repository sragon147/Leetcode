class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordList.add(endWord)
        queue = collections.deque([[beginWord, 1]])
        while queue:
            word, length = queue.popleft()
            if word == endWord:
                return length
            for i in range(len(word)):
                for c in 'abcdefghijklmnopqrstuvwxyz':
                    next_word = word[:i] + c + word[i+1:]
                    if next_word in wordList:
                        wordList.remove(next_word)
                        queue.append([next_word, length + 1])
        return 0
    
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordSet = set(wordList)
        if endWord not in wordSet:
            return 0

        beginSet = {beginWord}
        endSet = {endWord}
        distance = 1
        while beginSet and endSet:
            if len(beginSet) > len(endSet):
                beginSet, endSet = endSet, beginSet
                
            wordSet -= beginSet
            distance += 1
            newSet = set()
            for word in beginSet:
                for i in range(len(word)):
                    left, right = word[:i], word[i + 1:]
                    for c in string.ascii_lowercase:
                        newStr = left + c + right
                        if newStr in wordSet:
                            if newStr in endSet:
                                return distance
                            newSet.add(newStr)
            beginSet = newSet

        return 0