class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if len(word1) != len(word2):
            return False
        
        word_1_dict = {}
        word_2_dict = {}

        for i in range(0, len(word1)):
            if not word_1_dict.get(word1[i]):
                word_1_dict[word1[i]] = 1
            else:
                word_1_dict[word1[i]] += 1
        
        for i in range(0, len(word2)):
            char = word2[i]
            if not word_1_dict.get(char):
                return False
            if not word_2_dict.get(char):
                word_2_dict[char] = 1
            else:
                word_2_dict[char] += 1

        for _, frequency in word_1_dict.items():
            found_match = False
            for _, value in word_2_dict.items():
                if frequency == value:
                    found_match = True
                    continue
            if found_match == False:
                return False
        
        for _, frequency in word_2_dict.items():
            found_match = False
            for _, value in word_1_dict.items():
                if frequency == value:
                    found_match = True
                    continue
            if found_match == False:
                return False
        return True
    

s = Solution()
print(s.closeStrings("ccccaabbb", "aaabbbccc"))
print("-----")