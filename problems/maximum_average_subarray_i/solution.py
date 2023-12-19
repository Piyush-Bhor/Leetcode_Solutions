class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        i,j = 0, k - 1
        window_sum = sum(nums[:k])
        max_average = window_sum / k

        while j < (len(nums) - 1):
            j += 1
            window_sum = window_sum - nums[i] + nums[j]
            average = window_sum / k
            max_average = max(max_average, average)
            i += 1
        return max_average