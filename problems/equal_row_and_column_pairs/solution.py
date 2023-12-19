from collections import Counter

class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        n = len(grid)
        rows, cols = Counter(), Counter()
        pairs = 0

        for i in range(n):
            rows[tuple(grid[i])] += 1
            cols[tuple([grid[r][i] for r in range(n)])] += 1

        for key, value in rows.items():
            if key in cols:
                pairs += value * cols[key]
        
        return pairs

