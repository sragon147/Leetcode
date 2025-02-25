class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        def alphabetize(s: str) -> List[int]:
            alphabet = [0] * 26
            for c in s:
                alphabet[ord(c) - ord('a')] += 1
            return alphabet
        anagrams_map = {}
        for s in strs:
            key = tuple(alphabetize(s))
            if key in anagrams_map:
                anagrams_map[key].append(s)
            else:
                anagrams_map[key] = [s]
        return list(anagrams_map.values())
    
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap=defaultdict(list)

        for word in strs:
            s="".join(sorted(word))

            hashmap[s].append(word)
            
        return(list(hashmap.values()))