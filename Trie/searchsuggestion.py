from typing import List

class TrieNode:
    
    def __init__(self):
        self.children = {}
        self.suggestions = []
        self.is_end = False

class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        node = self.root
        for ch in word:
            if ch not in node.children:
                node.children[ch] = TrieNode()
            node = node.children[ch]
            if len(node.suggestions) < 3:
                node.suggestions.append(word)
        node.is_end = True

class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        products.sort()
        trie = Trie()
        for p in products:
            trie.insert(p)

        res = []
        node = trie.root
        found = True
        for ch in searchWord:
            if found and ch in node.children:
                node = node.children[ch]
                res.append(node.suggestions)
            else:
                found = False
                res.append([])
        return res