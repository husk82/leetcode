from typing import List

class Solution:
    def compress(self, chars: List[str]) -> int:
        i = 0 
        write = 0

        while i < len(chars):
            current = chars[i]
            count = 0

            while i < len(chars) and current == chars[i]:
                i += 1
                count += 1

            chars[write] = current
            write += 1

            if count > 1:
                for digit in str(count):
                    chars[write] = digit
                    write += 1

        return write
       
