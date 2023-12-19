class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        def merged(nums1,nums2,m):
            for i in range(m,len(nums1)):
                nums1[i] = nums2[0]
                nums2.pop(0)
            nums1.sort()
            return nums1
        return merged(nums1,nums2,m)
        