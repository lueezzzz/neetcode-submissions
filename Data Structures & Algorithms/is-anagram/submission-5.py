class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False

        frequencies = {}

        for i in range(len(s)):
            frequencies[s[i]] = frequencies.get(s[i], 0) + 1
            frequencies[t[i]] = frequencies.get(t[i], 0) - 1

        for frequency in frequencies.values():
            if frequency != 0:
                return False

        return True
        

        