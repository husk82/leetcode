class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        count = 0
        for i in range (0, k):
            if s[i] in "aeiou":
                count += 1
        maxVow = count
        for i in range (k, len(s)):
            if s[i] in "aeiou":
                count += 1
            if s[i-k] in "aeiou":
                count -= 1
            maxVow = max(maxVow, count)
        return maxVow
    
sol = Solution()

print(sol.maxVowels("a", 1))