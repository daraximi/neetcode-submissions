class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        point = 0
        for character in t:
            if point < len(s) and s[point] == character:
                point += 1
            if point == len(s):
                return True
        return False
        