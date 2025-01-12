class Solution:
    def numSpecialEquivGroups(self, words: List[str]) -> int:
        group = {}
        for word in words:
            alphabet = [0] * 26  # Reset alphabet for each word
            for i in range(len(word)):
                if i % 2 == 0:
                    alphabet[ord(word[i]) - ord('a')] += 2
                else:
                    alphabet[ord(word[i]) - ord('a')] += 1
            # Convert the alphabet list to a tuple to make it hashable
            alphabet_tuple = tuple(alphabet)
            if alphabet_tuple not in group:
                group[alphabet_tuple] = 1
            else:
                group[alphabet_tuple] += 1
        print(group)
        return len(group)

    def numSpecialEquivGroups(self, words: List[str]) -> int:
        seen = set()
        for word in words:
            even = word[::2]
            odd = word[1::2]
            key = str(sorted(even)) + str(sorted(odd))
            if key not in seen:
                seen.add(key)

        return len(seen)
