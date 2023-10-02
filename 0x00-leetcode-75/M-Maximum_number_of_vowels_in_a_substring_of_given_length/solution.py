class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        maximum = 0
        vowels_dict = {
            'a': True,
            'e': True,
            'i': True,
            'o': True,
            'u': True
        }
        l = 0
        count = 0
        for r in range(len(s)):
            if vowels_dict.get(s[r]):
                count += 1
            if r-l+1 > k:
                if vowels_dict.get(s[l]):
                    count -= 1
                l += 1
            maximum = max(maximum, count)
        return maximum
s = Solution()
print(s.maxVowels("leetcode", 3))

# solution: https://www.youtube.com/watch?v=kEfPSzgL-Ss