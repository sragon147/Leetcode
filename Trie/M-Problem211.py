from collections import deque


class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False

class WordDictionary:

    def __init__(self):
        self.root=TrieNode()

    def addWord(self, word: str) -> None:
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end_of_word = True

    def search(self, word: str) -> bool:
        queue = [self.root]
        for char in word:
            next_queue = []
            for node in queue:
                if char != ".": 
                    if char in node.children:
                        next_queue.append(node.children[char])
                else:
                    next_queue.extend(node.children.values())
            if not next_queue:
                return False
            queue = next_queue
        return any(node.is_end_of_word for node in queue)

class WordDictionary:

    def __init__(self):
        self.mem=defaultdict(set)
        self.visited={}

    def addWord(self, word: str) -> None:
        self.mem[len(word)].add(word)
        
    def search(self, word: str) -> bool:
        n=len(word)
        key=(word, len(self.mem[n]))
        if key in self.visited:
            return self.visited[key]
        for w in self.mem[n]:
            i=0
            while i<n and (word[i]==w[i] or word[i]=='.'):
                i+=1
            if i==n:
                self.visited[key]=True
                return True
        self.visited[key]=False
        return False
    
class TrieNode:
    def __init__(self):
        self.children = {}
        self.end_node = 0
        
class WordDictionary:
    def __init__(self):
        self.root = TrieNode()      

    def addWord(self, word):
        root = self.root
        for symbol in word:
            root = root.children.setdefault(symbol, TrieNode())
        root.end_node = 1
        
    def search(self, word):
        def dfs(node, i):
            if i == len(word): return node.end_node
               
            if word[i] == ".":
                for child in node.children:
                    if dfs(node.children[child], i+1): return True
                    
            if word[i] in node.children:
                return dfs(node.children[word[i]], i+1)
            
            return False
    
        return dfs(self.root, 0)
    
obj = WordDictionary()
obj.addWord("at")
obj.addWord("and")
obj.addWord("an")
obj.addWord("add")
param_2 = obj.search("and")