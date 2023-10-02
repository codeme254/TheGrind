from typing import List
class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        max_average = float('-inf')
        left = 0
        right = k - 1
        sum = 0
        for i in range(0, k):
            sum += nums[i]
        current_average = sum/k
        if current_average > max_average:
            max_average = current_average
        while right < len(nums)-1:
            right += 1
            sum += nums[right] - nums[left]
            current_average = sum / k
            if current_average > max_average:
                max_average = current_average
            left += 1
        return max_average

s = Solution()
# print(s.find_average([1,2,3],0,2))
print(s.findMaxAverage([1,12,-5,-6,50,3], 4))
print(s.findMaxAverage([5], 1))