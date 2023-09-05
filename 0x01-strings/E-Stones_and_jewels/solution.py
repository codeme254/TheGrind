class Solution(object):
    def numJewelsInStones(self, jewels, stones):
        """
        :type jewels: str
        :type stones: str
        :rtype: int
        """
        num_jewels = 0
        for i in range(0, len(jewels)):
            current_jewel_character = jewels[i]
            num_jewels += self.count_occurrences(current_jewel_character, stones)
        return num_jewels

    def count_occurrences(self, character, string):
        """counts how many time a character appears in a string"""
        if len(character) > 1 or not character:
            return 0
        occurrences = 0
        for i in range(0, len(string)):
            if string[i] == character:
                occurrences += 1
        return occurrences

solution = Solution()
print(solution.numJewelsInStones("aA", "aAAbbbb"))
print(solution.numJewelsInStones("z", "ZZ"))