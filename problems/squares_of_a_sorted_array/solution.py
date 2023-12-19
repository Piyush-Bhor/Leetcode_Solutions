class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        l2 = []
        for i in nums:
            squared_num = i * i
            l2.append(squared_num)
        l2.sort()
        return l2
        
        