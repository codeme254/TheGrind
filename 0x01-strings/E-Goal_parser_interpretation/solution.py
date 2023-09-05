class Solution(object):
    def interpret(self, command):
        """
        :type command: str
        :rtype: str
        """
        interpreted = ""
        for i in range(0, len(command)):
            current_character = command[i]
            if current_character == "G":
                interpreted += "G"
            elif current_character == "(":
                if command[i+1] == ")":
                    interpreted += "o"
                    i += 1
                elif command[i+1] == "a":
                    interpreted += "al"
                    i += 4
        return interpreted

solution = Solution()
print(solution.interpret("G()(al)"))
print(solution.interpret("G()()()()(al)"))
print(solution.interpret("(al)G(al)()()G"))