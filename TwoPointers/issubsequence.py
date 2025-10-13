class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i = j = found = 0
        if len(s) == 0 :
            return True
        for i in range (len(t)):
            if s[j] == t[i]:
                found += 1
                j += 1
            if found == len(s):
                return True
        return False
