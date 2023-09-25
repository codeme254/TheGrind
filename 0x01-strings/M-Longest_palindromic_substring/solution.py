class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if len(s) == 1:
            return 1
        
    
    def expand(self, index, string):
        """Finds the length of the longest substring from a given index"""
        left = index - 1
        right = index + 1
        while left >= 0 and right < len(string):
            if string[left] == string[right]:
                left -= 1
                right += 1
            else:
                return right - left
        return right - left - 1

https://leetcode.com/problems/longest-palindromic-substring/description/

https://leetcode.com/problems/longest-palindromic-substring/solutions/4005725/video-visualization-of-expand-from-centers-solution/