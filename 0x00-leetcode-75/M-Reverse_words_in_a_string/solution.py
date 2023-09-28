class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        s = s.strip()
        s_arr = self._split(s)
        reversed = ""
        main_str_ptr = len(s_arr) - 1
        reversed_str_ptr = len(reversed)

        while main_str_ptr >= 0:
            if len(reversed) > 0:
                if reversed[reversed_str_ptr] == "":
                    continue
            reversed += f"{s_arr[main_str_ptr]}"
            main_str_ptr -= 1
        return reversed
    
    def _split(self, string):
        """
        converts a string to an array based of spaces
        """
        result_arr = []
        string += ' '
        current_string = ""
        for i in range(0, len(string)):
            if string[i] != " ":
                current_string += string[i]
                if string[i + 1] == " ":
                    result_arr.append(current_string)
                    current_string = ""
            elif string[i] == " ":
                if result_arr[len(result_arr) - 1] == " ":
                    continue
                else:
                    result_arr.append(' ')
        result_arr.pop(len(result_arr) - 1)
        return result_arr

s = Solution()
print(s.reverseWords("a good   example           "))
