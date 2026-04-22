class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        res = 0
        stack = []

        for i in range(len(height)):
            while stack and height[i] > height[stack[-1]]:
                top = height[stack.pop()]
                if stack:
                    right = height[i]
                    left = height[stack[-1]]
                    h = min(right, left) - top
                    w = i - stack[-1] -1
                    res += h*w
            stack.append(i)

        return res
