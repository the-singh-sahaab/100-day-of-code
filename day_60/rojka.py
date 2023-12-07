class Solution:
    def isPossibleDivide(self, nums: List[int], k: int) -> bool:

        D = defaultdict(int)

        for x in nums:
            D[x] += 1

        for x in sorted(nums):
            if D[x] > 0:
                for i in range(k):
                    D[x + i] -= 1
        
        return len(set(list(D.values()))) == 1