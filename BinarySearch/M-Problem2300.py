from typing import List

class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        res = []
        potions = sorted(potions)
        potions_count = len(potions)
        for spell in spells:
            l = 0
            r = potions_count - 1
            while l <= r:
                m = l + (r - l) // 2
                strength = spell * potions[m]
                if strength < success:
                    l = m + 1
                else:
                    r = m - 1
            res.append(potions_count - l)
        
        return res
                