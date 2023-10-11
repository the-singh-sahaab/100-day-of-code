class Solution:
    def numOfStrings(self, patterns: List[str], word: str) -> int:
        a = 0
        for i in patterns:
            if i in word:
                a+=1
        return a