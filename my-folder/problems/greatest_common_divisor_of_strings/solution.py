class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        # The Euclidean algorithm
        def gcd(n1, n2):
            while n2:
                n1, n2 = n2, n1 % n2
            return n1
        
        if str1 + str2 != str2 + str1:
            return ""
        else:
            x_length = gcd(len(str1), len(str2))
            x = str1[:x_length]
            return x