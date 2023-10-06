from typing import List
class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        nums_1_table = {}
        nums_2_table = {}
        nums_1_set = set()
        nums_2_set = set()

        for i in range(0, len(nums1)):
            nums_1_table[nums1[i]] = True
        
        for i in range(0, len(nums2)):
            nums_2_table[nums2[i]] = True
        
        for i in range(0, len(nums1)):
            if not nums_2_table.get(nums1[i]):
                nums_1_set.add(nums1[i])
        
        for i in range(0, len(nums2)):
            if not nums_1_table.get(nums2[i]):
                nums_2_set.add(nums2[i])
        return [list(nums_1_set), list(nums_2_set)]

s = Solution()
print(s.findDifference([1,2,3], [2,4,6]))
print(s.findDifference([1,2,3,3], [1,1,2,2]))