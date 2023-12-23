class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        for inst in image:
            start = 0
            end = len(inst) - 1
            while start <= end:
                inst[start], inst[end] = inst[end], inst[start]
                if inst[start] == 1:
                    inst[start] = 0
                else:
                    inst[start] = 1
                if start != end:
                    if inst[end] == 1:
                        inst[end] = 0
                    else:
                        inst[end] = 1
                start += 1
                end -= 1
        return image