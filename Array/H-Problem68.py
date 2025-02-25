from typing import List
class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        def justify_line(wordCount, widthLeft, line) -> str:
            space = [0] * (wordCount)
            while wordCount > 1:
                spaceLen = widthLeft // (wordCount-1)
                space[wordCount-2] = space[wordCount-1] + spaceLen
                widthLeft -= spaceLen * (wordCount-1)
                wordCount -= 1
            if widthLeft > 0:
                space[0] = widthLeft

            justified_line = ''
            for i in range(len(line)):
                justified_line += line[i] + " " * space[i]
            return justified_line
        line = []
        wordCount = 0
        widthLeft = maxWidth
        res = []
        for word in words:
            if len(word) > widthLeft - wordCount:
                res.append(justify_line(wordCount, widthLeft, line))
                line = []
                widthLeft = maxWidth
                wordCount = 0

            line.append(word)
            widthLeft -= len(word)
            wordCount += 1

        res.append(" ".join(line) + " " * (widthLeft - wordCount + 1))
        print(res)
        return res

Solution().fullJustify(["What","must","be","acknowledgment","shall","be"], 16)