from typing import List
class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        nums_1_set = set(nums1)
        nums_2_set = set(nums2)
        return [
            list(set(nums1).difference(set(nums2))),
            list(set(nums2).difference(set(nums1)))
        ]
s = Solution()
print(s.findDifference([1,2,3], [2,4,6]))