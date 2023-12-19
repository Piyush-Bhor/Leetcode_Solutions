class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        def inter(nums1,nums2,table={}):
            final = []
            if len(nums2) > len(nums1):
                temp = nums1
                nums1 = nums2
                nums2 = temp
            for num1 in nums1:
                if num1 in table:
                    table[num1] += 1
                else:
                    table[num1] = 1
            for num in nums2:
                if num in table and table[num] > 0:
                    final.append(num)
                    table[num] -= 1
            return final
        return inter(nums1,nums2)
