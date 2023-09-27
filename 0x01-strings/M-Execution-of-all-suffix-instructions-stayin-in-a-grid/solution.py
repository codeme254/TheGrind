class Solution(object):
    def executeInstructions(self, n, startPos, s):
        """
        :type n: int
        :type startPos: List[int]
        :type s: str
        :rtype: List[int]
        """
        answer = []
        row = startPos[0]
        columns = startPos[1]
        startPos = startPos

        for i in range(0, len(s)):
            answer.append(0)
            startPos[0] = row
            startPos[1] = columns
            for j in range(i, len(s)):
                if s[j] == "R":
                    startPos[1] += 1
                    if startPos[1] < n:
                        answer[i] += 1
                    else:
                        break
                elif s[j] == "D":
                    startPos[0] += 1
                    if startPos[0] < n:
                        answer[i] += 1
                    else:
                        break
                elif s[j] == "L":
                    startPos[1] -= 1
                    if startPos[1] >= 0:
                        answer[i] += 1
                    else:
                        break
                elif s[j] == "U":
                    startPos[0] -= 1
                    if startPos[0] >= 0:
                        answer[i] += 1
                    else:
                        break
        return answer

s = Solution()
print(s.executeInstructions(3, [0, 1], "RRDDLU"))
                