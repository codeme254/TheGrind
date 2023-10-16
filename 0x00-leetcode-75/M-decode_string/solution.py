class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        for i in range(len(s)):
            if s[i] != "]":
                stack.append(s[i])
            else:
                substr = ""
                while stack[-1] != '[':
                    substr = stack.pop() + substr
                stack.pop()
                k = ""
                while stack and stack[-1].isdigit():
                    k = stack.pop() + k
                stack.append(substr * int(k))
        return "".join(stack)
s = Solution()
print(s.decodeString("3[a]2[bc]"))
print(s.decodeString("3[a2[c]]"))
print(s.decodeString("2[abc]3[cd]ef"))
# solution to this problem https://youtu.be/qB0zZpBJlh8