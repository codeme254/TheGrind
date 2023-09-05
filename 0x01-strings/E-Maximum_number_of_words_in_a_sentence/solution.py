class Solution(object):
    def mostWordsFound(self, sentences):
        """
        :type sentences: List[str]
        :rtype: int
        """
        maximum = 0
        for sentence in sentences:
            current_count = self.count_words_in_sentence(sentence)
            if current_count > maximum:
                maximum = current_count
        return maximum
    
    def count_words_in_sentence(self, sentence):
        """Returns the number of words in a sentence"""
        return len(sentence.split())

solution = Solution()
print(solution.mostWordsFound(["alice and bob love leetcode", "i think so too", "this is great thanks very much"]))