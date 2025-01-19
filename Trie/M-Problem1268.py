import bisect
from typing import List
class Trie:

    def __init__(self):
        self.trie = {}

    def insert(self, word: str) -> None:
        t = self.trie
        for w in word:
            if w not in t:
                t[w] = {}
            t = t[w]
        t["end"] = True 

    def search(self, searchWord: str) -> List[str]:
        t = self.trie
        for w in searchWord:
            if w in t:
                t = t[w]
            else:
                return []  # If no such prefix exists, return an empty list
        
        ans = []
        
        def dfs(n, product):
            # If we reach an "end" marker, add the word to the result
            if "end" in n:
                ans.append(product)
            
            # Iterate through the child nodes of the current node
            for key in n:
                if key != "end":
                    dfs(n[key], product + key)
        # Start DFS from the current node (t) with the prefix searchWord
        dfs(t, searchWord)
        return sorted(ans)[:3]
        

class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        trie = Trie()
        for product in products:
            trie.insert(product)
        res = []
        for i in range(1, len(searchWord) + 1):
            res.append(trie.search(searchWord[:i]))
        return res
    
    def suggestedProducts2(self, products: List[str], searchWord: str) -> List[List[str]]:
        def bisect_left_helper(arr: List[str], target: str) -> int:
            """Find the leftmost position to insert target in sorted arr."""
            low, high = 0, len(arr)
            while low < high:
                mid = (low + high) // 2
                if arr[mid] < target:
                    low = mid + 1
                else:
                    high = mid
            return low
        
        products.sort()
        cur, ans = '', []
        for char in searchWord:
            cur += char
            # Treat searchWord as a product, using bisect(binary search) 
            # to find the position of product searchWord while maintain the sorted order of the List 
            i = bisect_left_helper(products, cur)
            # i = bisect.bisect_left(products, cur)
            ans.append([product for product in products[i : i + 3] if product.startswith(cur)])
        return ans
Solution().suggestedProducts2(["mobile","mouse","moneypot","monitor","mousepad"], "mouse")