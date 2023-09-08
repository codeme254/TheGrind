class Solution(object):
    def kthDistinct(self, arr, k):
        """
        :type arr: List[str]
        :type k: int
        :rtype: str
        """
        if len(arr) == 0:
            return ""
        seen_strings = {}
        distinct_count = 0
        current_distinct = ""
        distinct_strings_stack = []
        for string in arr:
            if seen_strings.get(string):
                current_distinct = ""
                distinct_count -= 1
            else:
                distinct_count += 1
                if distinct_count <= k:
                    current_distinct = string
            seen_strings[string] = True
        print(seen_strings)
        return current_distinct

s = Solution()
print(s.kthDistinct(["aa", "aa", "a", "aaa", "a", "b"], 1))
