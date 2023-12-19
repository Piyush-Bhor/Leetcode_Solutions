class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        i, j, count, max_count = 0, 0, 0, 0

        while j < len(s):
            if s[j] in 'aeiou':
                count += 1
            if (j - i) + 1 == k:
                max_count = max(max_count, count)
                if s[i] in 'aeiou':
                    count -= 1
                i += 1
            j += 1
        return max_count