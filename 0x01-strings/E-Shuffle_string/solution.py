class Solution(object):
    def restoreString(self, s, indices):
        """
        :type s: str
        :type indices: List[int]
        :rtype: str
        """
        final_list = [""]*len(s)
        current_list_index = 0
        current_string_index = 0
        while current_list_index < len(indices):
            final_list[indices[current_list_index]] = s[current_string_index]
            current_list_index += 1
            current_string_index += 1
        return "".join(final_list)

s = Solution()
print(s.restoreString("codeleet", [4,5,6,7,0,2,1,3]))
