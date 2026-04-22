class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        checker = {
            "}":"{",
            "]":"[",
            ")":"("
        }
        if len(s)<2:
            return False
        for char in s:
            if char in checker:
                if stack and stack[-1] == checker[char]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(char)
        return True if not stack else False
        