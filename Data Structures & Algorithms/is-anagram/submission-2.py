class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        s = sorted(s)
        t = sorted(t)
        
        for char in range(len(s)):
            if s[char] != t[char]:
                return False
        return True
        