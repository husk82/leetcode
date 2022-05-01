class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(t) != len(s):
            return False
        if sorted(s) == sorted(t):
            return True
        return False