class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        for i in range(0, len(flowerbed)):
            if self.flower_can_fit(flowerbed, i):
                n -= 1
                flowerbed[i] = 1
        return n <= 0
    
    def flower_can_fit(self, flowerBed, index):
        """
        Checks if a flower can be placed at a given index
        returns True if it can and False otherwise
        """
        if len(flowerBed) == 1 and flowerBed[0] == 1:
            return False
        if len(flowerBed) == 1 and flowerBed[0] == 0:
            return True
        if flowerBed[index] == 1:
            return False
        
        if index == 0:
            if flowerBed[1] == 1:
                return False
            return True
        if index == len(flowerBed) - 1:
            if flowerBed[len(flowerBed) - 2] == 1:
                return False
            return True
        if flowerBed[index + 1] == 1 or flowerBed[index - 1] == 1:
            return False
        return True

s = Solution()
print(s.canPlaceFlowers([1,0,0,0,1], 2))