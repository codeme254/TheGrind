class Solution(object):
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """
        s = ""
        if len(chars) == 1:
            return 1
        
        i = 0
        count = 1
        while i < len(chars)-1:
            current_char = chars[i]
            next_char = chars[i+1]
            if current_char == next_char:
                count += 1
            else:
                if count > 1:
                    s += "{}{}".format(current_char,count)
                    chars.insert()
                else:
                    s += current_char
                count = 1
            i += 1
        # print(chars[i], count)
        if chars[i] == chars[i-1]:
            s += "{}{}".format(chars[i], count)
        else:
            s += "{}".format(chars[i])
        
        i = len(s) - 1
        while i >= 0:
            chars.insert(0, s[i])
            i -= 1
        # print(chars)
        return len(s)
    
s = Solution()
print(s.compress(["a","a","b","b","c","c","c"]))
