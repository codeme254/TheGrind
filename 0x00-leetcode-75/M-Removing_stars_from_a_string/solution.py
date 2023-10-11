class Solution:
    def removeStars(self, s: str) -> str:
        stack = []
        for i in range(0, len(s)):
            if s[i] == "*":
                if len(stack) == 0:
                    continue
                stack.pop()
            else:
                stack.append(s[i])
        return "".join(stack)
s = Solution()
print(s.removeStars("leet**cod*e"))
print(s.removeStars("erase*****"))
print(s.removeStars("**********"))