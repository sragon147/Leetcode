from typing import List
from collections import defaultdict

class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = None

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word: str):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.word = word

class Solution:
    def __init__(self):
        self.trie = Trie()
        self.result = set()
    
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        rows, cols = len(board), len(board[0])
        
        for word in words:
            self.trie.insert(word)

        def dfs(r, c, node):
            char = board[r][c]
            if char not in node.children:
                return
            
            next_node = node.children[char]
            if next_node.word:
                self.result.add(next_node.word)
            
            board[r][c] = "#"
            for dr, dc in [(0,1), (1,0), (0,-1), (-1,0)]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and board[nr][nc] != "#":
                    dfs(nr, nc, next_node)
            board[r][c] = char

        for r in range(rows):
            for c in range(cols):
                dfs(r, c, self.trie.root)
        
        return list(self.result)

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        trie = {}
        WORD = "@"
        ROWS = len(board) - 1
        COLS = len(board[0]) - 1
        for word in words:
            root = trie
            for char in word:
                root = root.setdefault(char, {})
            root[WORD] = word

        res = []
        def dfs(r = 0, c = 0, root = trie):
            char = board[r][c]
            if char not in root:
                return
            
            prev_root = root
            root = root[char]
            board[r][c] = '#'
            if WORD in root:
                res.append(root[WORD])
                root.pop(WORD)
            
            if c > 0: dfs(r, c - 1, root)
            if c < COLS: dfs(r, c + 1, root)
            if r < ROWS: dfs(r + 1, c, root)
            if r > 0: dfs(r - 1, c, root)
            board[r][c] = char
            if not root:
                prev_root.pop(char)
            
        for r in range(len(board)):
            for c in range(len(board[r])):
                dfs(r, c)
        
        return res
    
class Solution:
    
    def find(self, word, i, j):
        if len(word) == 0:
            return True
        if (not 0 <= i < len(self.board)) or (not 0 <= j < len(self.board[0])) or word[0] != self.board[i][j] or self.visited[i][j]:
            return False
        self.visited[i][j] = True
        ans = self.find(word[1:], i + 1, j) or self.find(word[1:], i, j + 1) or self.find(word[1:], i - 1, j) or self.find(word[1:], i, j - 1)
        self.visited[i][j] = False
        return ans
    
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        self.board = board
        self.visited = [[False for _ in range(len(board[0]))] for _ in range(len(board))]
        self.m = defaultdict(list)
        for i in range(len(board)):
            for j in range(len(board[0])):
                self.m[self.board[i][j]].append((i, j))
        ans = []
        reverse = len(set(word[:len(word) // 2] for word in words)) < 2
        for word in words:
            word = word[::-1] if reverse else word
            for i, j in self.m[word[0]]:
                if self.find(word, i, j):
                    ans.append(word[::-1] if reverse else word)
                    break
        return ans