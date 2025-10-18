from collections import Counter

class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        count1 = Counter(word1)
        count2 = Counter(word2)

        keys1 = list(count1.keys())
        keys2 = list(count2.keys())

        freq1 = list(count1.values())
        freq2 = list(count2.values())

        if set(keys1) != set(keys2):
            return False
        if sorted(freq1) != sorted(freq2):
            return False
        
        return True