class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        def pali(s):
            s = ''.join(e for e in s if e.isalnum()).lower()
            l = 0
            r = len(s) - 1
            while r > l:
                if s[l] != s[r]:
                    return False
                    break
                l += 1
                r -= 1
            return True
        return pali(s)