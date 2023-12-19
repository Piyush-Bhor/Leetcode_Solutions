class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        can_plant = 0
        i = 0
        while i < len(flowerbed):
            if flowerbed[i] == 0 and (i == 0 or flowerbed[i - 1] == 0) and (i == len    (flowerbed) - 1 or flowerbed[i + 1] == 0):
                can_plant += 1
                flowerbed[i] = 1
                if can_plant >= n:
                    return True
            i += 1
        return can_plant >= n