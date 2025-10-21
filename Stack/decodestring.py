class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        curNum = 0
        curStr = ""
        for c in s:
            if c.isdigit():
                curNum = (curNum * 10) + int(c)
            elif c.isalpha():
                curStr += c
            elif c == '[':
                stack.append((curStr, curNum))
                curStr = ""
                curNum = 0
            else:
                print(stack)
                prevStr, num = stack.pop()
                curStr = prevStr + curStr * num
        return curStr
    
sol = Solution()

print(sol.decodeString("3[a]2[bc]"))
print(sol.decodeString("3[a2[c]]"))