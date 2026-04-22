class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n = len(nums)
        res = float("inf")
        l = 0
        total = 0
        for r in range(n):
            total += nums[r]
            while total >= target:
                res = min(r- l + 1, res)
                total -= nums[l]
                l += 1

        return 0 if res == float("inf") else res