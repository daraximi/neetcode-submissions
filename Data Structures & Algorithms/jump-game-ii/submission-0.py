class Solution:
    def jump(self, nums: List[int]) -> int:
        res = 0
        # Instead of going forwards you can go backwards and ask yourself the question can you reach 
        # index 0 from index n-1
        n = len(nums)
        l , r = 0 , 0
        while r < n - 1:
            farthest = 0
            for i in range(l, r + 1):
                farthest = max(farthest, i + nums[i])
            l = r + 1
            r = farthest
            res += 1
        return res
        