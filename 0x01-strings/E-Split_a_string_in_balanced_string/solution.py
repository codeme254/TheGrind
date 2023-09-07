class Solution(object):
    def balancedStringSplit(self, s):
        """
        :type s: str
        :rtype: int
        """
        total_splits = 0
        current_string = ""
        for i in range(0, len(s)):
            current_character = s[i]
            current_string += current_character
            if self.is_balanced_string(current_string):
                total_splits += 1
                current_string = ""
        return total_splits
    def is_balanced_string(self, string):
        number_of_Ls = 0
        number_of_Rs = 0
        for i in range(0, len(string)):
            current_character = string[i]
            if current_character == "L":
                number_of_Ls += 1
            elif current_character == "R":
                number_of_Rs += 1
        return number_of_Rs == number_of_Ls

solution = Solution()
print(solution.balancedStringSplit("RLRRLLRLRL"))
print(solution.balancedStringSplit("RLRRRLLRLL"))
print(solution.balancedStringSplit("LLLLRRRR"))