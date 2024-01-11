class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        n = []
        for i in arr:
            if arr.count(i) < 2:
                n.append(i)

        if len(n) >= k:
            return n[k-1]
        else:
            return ""