from typing import List
class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        max_area = 0
        while left < right:
            current_area = (right - left) * min(height[left], height[right])
            if current_area > max_area:
                max_area = current_area
            # alter the pointer that is pointing to the smallest height
            # we want to keep maintaining the greatest height as it is likely to give us the best result
            # if they are both equal, increment any of them
            if height[left] > height[right]:
                right -= 1
            elif height[right] > height[left]:
                left += 1
            else:
                left += 1
        return max_area
    
s = Solution()
print(s.maxArea([1,1]))