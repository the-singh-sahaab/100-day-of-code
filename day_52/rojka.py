class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        refund =  []
        cost   = 0
        for i in costs:
            cost+=i[0]
            refund.append(i[1] - i[0])
        refund.sort()   
        for i in range(len(costs)//2):
            cost +=  refund[i]
        return cost


        