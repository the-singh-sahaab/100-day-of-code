class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        arr1 = list(set(arr))
        for i in arr1:
            if (arr.count(i))> len(arr)//4:
                return i
        return -1
        