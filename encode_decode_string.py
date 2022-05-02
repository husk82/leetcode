class Solution:
    """
    @param: strs: a list of strings
    @return: encodes a list of strings to a single string.
    """
    def encode(strs):
        astring = ''
        for s in strs:
            astring += str(len(s)) + '#' + s
        return astring

    """
    @param: str: A string
    @return: dcodes a single string to a list of strings
    """
    def decode(encoded_str):
        alist = []
        i = 0
        while i < len(encoded_str):
            if encoded_str[i] == '#':
                length = int(encoded_str[i-1])
                alist.append(encoded_str[i+1: length + i + 1])
                i = length + i + 1
            i += 1
        return alist
    
    
    def decode2(str):
        res, i = [], 0
        while i < len(str):
            j = i
            print(i, j, res)
            while str[j] != "#":
                j += 1
            length = int(str[i:j])
            res.append(str[j + 1 : j + 1 + length])
            i = j + 1 + length
        return res
    
