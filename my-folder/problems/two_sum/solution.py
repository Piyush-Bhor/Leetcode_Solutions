class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashTable = dict()
        for i in range(len(nums)):
            diff = target - nums[i]
            if nums[i] in hashTable:
                return(hashTable[nums[i]], i)
            else:
                hashTable[diff] = i