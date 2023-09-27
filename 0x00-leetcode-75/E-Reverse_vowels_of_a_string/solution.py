class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        vowels = {
            'a': True,
            'e': True,
            'i': True,
            'o': True,
            'u': True,
            'A': True,
            'E': True,
            'I': True,
            'O': True,
            'U': True
        }

        s_arr = list(s)
        left = 0
        right = len(s_arr)-1
        while left < right:
            while not vowels.get(s_arr[left]):
                left += 1
                if left >= len(s_arr):
                    break
            while not vowels.get(s_arr[right]):
                right -= 1
                if right < 0:
                    break
            if left < right and (vowels.get(s_arr[left]) and vowels.get(s_arr[right])):
                temp = s_arr[left]
                s_arr[left] = s_arr[right]
                s_arr[right] = temp
            left += 1
            right -= 1
        return "".join(s_arr)