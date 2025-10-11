class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = ['a', 'e', 'i' , 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        left = 0
        right = len(s) - 1
        chars = list(s)

        while left < right:
            if chars[left] in vowels and chars[right] in vowels:
                chars[left], chars[right] = chars[right], chars[left]
                left += 1
                right -= 1
            elif chars[left] in vowels:
                right -= 1
            elif chars[right] in vowels:
                left += 1
            else:
                left += 1
                right -= 1
        
        return "".join(chars)