class Solution(object):
    def finalValueAfterOperations(self, operations):
        """
        :type operations: List[str]
        :rtype: int
        """
        x = 0
        for value in operations:
            if value == "X++" or value == "++X":
                x += 1
            elif value == "X--" or value == "--X":
                x -= 1
        return x

solution = Solution()
print(solution.finalValueAfterOperations(["--X","X++","X++"]))
print(solution.finalValueAfterOperations(["++X","++X","X++"]))
print(solution.finalValueAfterOperations(["X++","++X","--X","X--"]))