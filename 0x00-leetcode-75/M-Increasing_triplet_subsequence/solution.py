import sys
class Solution(object):
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        i = sys.maxsize
        j = sys.maxsize
        k = sys.maxsize
        if len(nums) < 3:
            return False
        for i in range(0, len(nums)):
            if nums[i] <= i:
                i = nums[i]
            elif nums[i] <= j:
                j = nums[i]
            else:
                return True
        return False

s = Solution()
# print(s.increasingTriplet([2,4,-2,-3]))
print(s.increasingTriplet([1,5,0,4,1,3]))