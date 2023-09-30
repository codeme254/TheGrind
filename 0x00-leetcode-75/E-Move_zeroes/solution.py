from typing import List
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        left_ptr = 0
        for right_ptr in range(len(nums)):
            if nums[right_ptr]:
                nums[right_ptr], nums[left_ptr] = nums[left_ptr], nums[right_ptr]
                left_ptr += 1
    
    def swap(self, index1, index2, arr):
        """
        swaps two elements of an array in place
        """
        temp = arr[index1]
        arr[index1] = arr[index2]
        arr[index2] = temp

nums = [12, 1, 0, 9, 3, 0, 0, 0]
s = Solution()
print(s.moveZeroes(nums))
print(nums)

# solution to this problem: https://www.youtube.com/watch?v=aayNRwUN3Do