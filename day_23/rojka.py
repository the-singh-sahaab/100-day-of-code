class Solution:
    def splitWordsBySeparator(self, words: List[str], separator: str) -> List[str]:
        new = []
        for i in words:
            new += i.split(separator)

        while "" in new:
            new.remove("") 
        return new
        