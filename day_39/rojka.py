
class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        first = 0
        second = 0
        ans = ['']
        def win(nums, first, second, ans):
            nums_copy = nums.copy()
            if len(nums_copy) == 0:
                if first >= second:
                    ans[0] = 'first'
                    return
                else:
                    ans[0] = 'second'
                    return
            if nums_copy[0] > nums_copy[-1]:
                if len(nums_copy) < 2:
                    first+=nums_copy[0]
                    nums_copy.pop(0)
                else:    
                    if nums_copy[1] >= nums_copy[-2] and nums_copy[1]+nums_copy[-1] > nums_copy[0] + nums_copy[-2]:
                        first+=nums_copy[-1]
                        nums_copy.pop(-1)
                    else:
                        first+=nums_copy[0]
                        nums_copy.pop(0)
            else:
                if len(nums_copy) < 2:
                    first+=nums_copy[0]
                    nums_copy.pop(0)
                else:
                    if nums_copy[1] <= nums_copy[-2] and nums_copy[1]+nums_copy[-1] < nums_copy[0] + nums_copy[-2]:
                        first+=nums_copy[0]
                        nums_copy.pop(0)
                    else:
                        first+=nums_copy[-1]
                        nums_copy.pop(-1)
            if len(nums_copy) == 0:
                if first >= second:
                    ans[0] = 'first'
                    return
                else:
                    ans[0] = 'second'
                    return
            if nums_copy[0] > nums_copy[-1]:
                if len(nums_copy) < 2:
                    second+=nums_copy[0]
                    nums_copy.pop(0)
                else:
                    if nums_copy[1] >= nums_copy[-2] and nums_copy[1]+nums_copy[-1] > nums_copy[0] + nums_copy[-2]:
                        second+=nums_copy[-1]
                        nums_copy.pop(-1)
                    else:
                        second+=nums_copy[0]
                        nums_copy.pop(0)
            else:
                if len(nums_copy) < 2:
                    second+=nums_copy[0]
                    nums_copy.pop(0)
                else:
                    if nums_copy[1] <= nums_copy[-2] and nums_copy[1]+nums_copy[-1] < nums_copy[0] + nums_copy[-2]:
                        second+=nums_copy[0]
                        nums_copy.pop(0)
                    else:
                        second+=nums_copy[-1]
                        nums_copy.pop(-1)
            win(nums_copy, first, second, ans)
        win(nums, 0, 0, ans)
        if ans[0] == 'first':
            return True
        else:
            return False