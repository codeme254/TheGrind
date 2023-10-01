from typing import List
class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        if len(nums) <= 1:
            return 0
        pairs = 0
        nums = sorted(nums)
        left = 0
        right = len(nums) - 1
        while left < right:
            if nums[left] + nums[right] == k:
                left += 1
                right -= 1
                pairs += 1
            elif nums[left] + nums[right] > k:
                right -= 1
            elif nums[left] + nums[right] < k:
                left += 1
        return pairs

s = Solution()
print(s.maxOperations([1,2,3,4],5))


