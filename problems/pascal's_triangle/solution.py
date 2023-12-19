class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        def nextRow(tri):
            for s in tri:
                l2 = []
                if len(s) > 1:
                    l2.append(s[0])
                    for i in range(len(s)-1):
                        num = s[i] + s[i+1]
                        l2.append(num)
                    l2.append(s[len(s)-1])
            tri.append(l2)
            return tri
    
        def pascal(nRow):
            tri = [[1],[1,1]]
            if nRow == 1:
                return [[1]]
            elif nRow == 2:
                return [[1],[1,1]]
            else: 
                count = 0
                n = nRow - 3
                while count <= n:
                    nextRow(tri)
                    count += 1
                return tri
        
        return pascal(numRows)