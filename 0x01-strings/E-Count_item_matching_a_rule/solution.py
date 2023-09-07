class Solution(object):
    def countMatches(self, items, ruleKey, ruleValue):
        """
        :type items: List[List[str]]
        :type ruleKey: str
        :type ruleValue: str
        :rtype: int
        """
        found = 0
        for item in items:
            if self.is_present_in_array(item, ruleKey, ruleValue):
                found += 1
        return found
    
    def is_present_in_array(self, array, key, value):
        search_index = 0
        if key == "type":
            search_index = 0
        elif key == "color":
            search_index = 1
        elif key == "name":
            search_index = 2
        else:
            return None
        return array[search_index] == value

s = Solution()
print(s.countMatches([["phone","blue","pixel"],["computer","silver","phone"],["phone","gold","iphone"]], "type", "phone"))