from typing import List
class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        highest_altitude = 0
        running_sum = 0
        for i in range(0, len(gain)):
            running_sum += gain[i]
            highest_altitude = max(highest_altitude, running_sum)
        return highest_altitude

s = Solution()
print(s.largestAltitude([-5,1,5,0,-7]))
print(s.largestAltitude([-4,-3,-2,-1,4,3,2]))