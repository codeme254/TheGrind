class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        left = 0
        right = 0
        final_str = ""
        current_turn = "l"

        while left < len(word1) and right < len(word2):
            if current_turn == "l":
                final_str += word1[left]
                left += 1
                current_turn = "r"
            elif current_turn == "r":
                final_str += word2[right]
                right += 1
                current_turn = "l"
        
        while left < len(word1):
            final_str += word1[left]
            left += 1
        
        while right < len(word2):
            final_str += word2[right]
            right += 1
        return final_str

s = Solution()
print(s.mergeAlternately("abcd", "pq"))