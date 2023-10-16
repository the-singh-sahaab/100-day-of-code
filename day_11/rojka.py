class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        arrOdd , arrEven =[] , []
        for num in nums:
            if num%2==0:
                arrEven.append(num)
            else:
                arrOdd.append(num)
    
        #print(arrEven,arrOdd)
        res = []
        for i in range(len(arrEven)):
            res.append(arrEven[i])
            res.append(arrOdd[i])
    
        return res
        