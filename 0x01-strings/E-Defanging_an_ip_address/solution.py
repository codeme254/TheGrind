"""Defanging an ip address"""
class Solution(object):
    def defangIPaddr(self, address):
        """
        :type address: str
        :rtype: str
        """
        final_address:str = ""
        for i in range(0, len(address)):
            if address[i] == ".":
                final_address += "[.]"
            else:
                final_address += address[i]
        return final_address

solution: Solution = Solution()
print(solution.defangIPaddr("255.100.50.0"))