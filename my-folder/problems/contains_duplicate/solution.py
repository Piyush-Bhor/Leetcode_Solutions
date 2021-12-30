class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hashTable = {}
        for i in nums:
            if i not in hashTable:
                hashTable[i] = 1
            else:
                return True
        return False
            