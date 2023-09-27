class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        """
        :type candies: List[int]
        :type extraCandies: int
        :rtype: List[bool]
        """
        result = []
        greatest_number_of_candies = self.greatest_number_of_candies(candies)
        for i in range(0, len(candies)):
            if candies[i] + extraCandies >= greatest_number_of_candies:
                result.append(True)
            else:
                result.append(False)
        return result
    
    def greatest_number_of_candies(self, candies):
        """
        finds the greatest number of candies in an array of candies
        """
        greatest_number = 0
        for i in range(0, len(candies)):
            if candies[i] > greatest_number:
                greatest_number = candies[i]
        return greatest_number

s = Solution()
print(s.kidsWithCandies([2,3,5,1,3], 3))