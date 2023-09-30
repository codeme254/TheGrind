class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s) == 0 and len(t) == 0:
            return True
        if len(s) == 0:
            return True
        
        s_ptr = 0
        t_ptr = 0
        while t_ptr < len(t):
            if s[s_ptr] == t[t_ptr]:
                s_ptr += 1
                if s_ptr >= len(s):
                    return True
            t_ptr += 1
        return False

s = Solution()
print(s.isSubsequence("abc", "ahbgdc"))