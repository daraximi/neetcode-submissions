class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n, l , total = len(nums), 0 , 0
        res = float('inf')

        for r in range(n):
            total += nums[r]
            while total >= target:
                res = min(r - l + 1, res)
                total -= nums[l]
                l += 1

        return 0 if res == float('inf') else res