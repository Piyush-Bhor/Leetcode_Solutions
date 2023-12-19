class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        def pali(num):
            og_num = num
            rev = 0
            while(num > 0):
                rev = (rev * 10) + (num % 10)
                num = int(num/10)
            if og_num == rev:
                return True
            else:
                return False
        return pali(x)
