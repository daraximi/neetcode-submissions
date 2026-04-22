class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) ==1:
            return nums[0]
        memo = [-1] * len(nums)

        def dfs(i, end):
            if i >= end:
                return 0
            if memo[i] != -1:
                return memo[i]
            memo[i] = max(dfs(i+1, end), nums[i] + dfs(i + 2, end))
            return memo[i]
        

        case1 = dfs(0, len(nums)-1)
        memo = [-1] * len(nums)
        case2 = dfs(1, len(nums))

        return max(case1,case2)
        