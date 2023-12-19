class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        def duplicate(nums,hash_table={}):
            for i in nums:
                if i in hash_table:
                    return True
                    break
                else:
                    hash_table[i] = 1
            return False
        return duplicate(nums)