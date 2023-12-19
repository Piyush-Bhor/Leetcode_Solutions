class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        def maxSumSubArr(nums):
            maxsum = -100000
            cursum = 0
            n = len(nums)
            for i in range(n):
                cursum+= nums[i]
                if (cursum>maxsum):
                    maxsum = cursum
                if (cursum<0):
                    cursum = 0
            return maxsum
        return maxSumSubArr(nums)