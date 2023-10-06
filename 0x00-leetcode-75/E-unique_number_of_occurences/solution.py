from typing import List
class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        occurrences_count = {}
        occurrences_lookup = {}
        for number in arr:
            if not occurrences_count.get(number):
                occurrences_count[number] = 1
            else:
                occurrences_count[number] += 1
        for _, value in occurrences_count.items():
            if occurrences_lookup.get(value):
                return False
            occurrences_lookup[value] = True
        return True
s = Solution()
print(s.uniqueOccurrences([1,2,2,1,1,3]))
print(s.uniqueOccurrences([1,2]))
print(s.uniqueOccurrences([-3,0,1,-3,1,1,1,-3,10,0]))