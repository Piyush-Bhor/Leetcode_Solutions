class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        left, total_sum = 0, sum(nums)

        for i in range(len(nums)):

            if left == total_sum - nums[i] - left:
                return i
            
            left += nums[i]

        return -1