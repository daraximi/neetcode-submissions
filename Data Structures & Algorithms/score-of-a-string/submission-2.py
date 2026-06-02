class Solution:
    def scoreOfString(self, s: str) -> int:
        i, j = 0, 1
        res = 0
        # if 0 < len(s) < 2:
        #     res = abs(ord(s[0]))
        while j < len(s):
            if j>=len(s):
                res += 0
            else:
                res += abs(ord(s[i]) - ord(s[j]))
            i, j = i + 1, j + 1
        return res