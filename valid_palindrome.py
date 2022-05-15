class Solution:
    def isPalindrome(self, s: str) -> bool:
        filtered = ''
        for c in s:
            if c.isalnum():
                filtered += c.lower()
        if filtered == filtered[::-1]:
            return True
        return False