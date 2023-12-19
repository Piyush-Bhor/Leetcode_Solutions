class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        def plusOneRecurse(nums,last):
            if nums[last] != 9:
                nums[last] = nums[last] + 1
                return nums
            elif nums[last] == 9:
                nums[last] = 0
                last -= 1
                return plusOneRecurse(nums,last)
            return nums
        
        def plusOnefinal(nums):
            nums.insert(0,0)
            last = len(nums)-1
            nums_final = plusOneRecurse(nums,last)
            if nums_final[0] == 0:
                nums_final.pop(0)
                return nums_final
            else:
                return nums_final
        
        return plusOnefinal(digits)
