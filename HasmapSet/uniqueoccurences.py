from typing import List
from collections import Counter

class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        count = Counter(arr)
        fre_values = list(count.values())
        return len(fre_values) == len(set(fre_values))