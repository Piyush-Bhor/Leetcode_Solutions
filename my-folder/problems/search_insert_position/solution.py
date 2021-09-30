class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        for i in range(0, len(nums)):
            if len(nums) == 1:
                if target < nums[i]:
                    return i
                elif target > nums[i]:
                    return i + 1
            if nums[i] == target:
                return i
            elif nums[i] < target and nums[i+1] > target:
                return i + 1   
            elif target > nums[len(nums) - 1]:
                return len(nums)
            elif nums[0] > target: 
                return 0
        
                
            