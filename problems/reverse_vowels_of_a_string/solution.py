class Solution:
    def reverseVowels(self, s: str) -> str:
        s = list(s)
        n = len(s)
        i = 0
        j = n - 1
        vowels = "aeiouAEIOU"
        while i < j:
            while i < j and s[i] not in vowels:
                i += 1
                continue
            while i < j and s[j] not in vowels:
                j -= 1
                continue
            s[i], s[j] = s[j], s[i]
            i += 1
            j -= 1
        return ''.join(s)
        