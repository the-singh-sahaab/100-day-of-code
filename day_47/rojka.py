class Solution:
    def interchangeableRectangles(self, rec: List[List[int]]) -> int:
        ratios = {}
        count = 0
        for [w, h] in rec:
            rect = w / h
            if rect not in ratios:
                ratios[rect] = 1
            else:
                count += ratios[rect]#adding to get the total number
                ratios[rect] += 1
        return count
        