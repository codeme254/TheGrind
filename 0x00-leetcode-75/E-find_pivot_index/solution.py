from typing import List
class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
        running_sum = 0
        summation = 0
        for i in range(0, len(nums)):
            summation += nums[i]
        
        for i in range(0, len(nums)):
            temp_summation = summation
            result = temp_summation - nums[i] - running_sum
            if result == running_sum:
                return i
            running_sum += nums[i]
        return -1
s = Solution()
print(s.pivotIndex([1,7,3,6,5,6]))
print(s.pivotIndex([1,2,3]))
print(s.pivotIndex([2,1,-1]))