class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        if len(s) != len(t):
            return False
    
        frequencies = {}

        for char in s:
            frequencies[char] = frequencies.get(char, 0) + 1

        for char in t:
            frequencies[char] = frequencies.get(char, 0) - 1

        for frequency in frequencies.values():
            if frequency != 0:
                return False

        return True

        # s = sorted(s)
        # t = sorted(t)

        # return s == t