class Solution:
    def reverseWords(self, s: str) -> str:
        word_list = s.split()
        return " ".join(reversed(word_list))

sol = Solution()

print(sol.reverseWords("  hello world  "))