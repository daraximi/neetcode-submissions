class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        l, r = 0, 0
        for i in range(len(nums)):
            if nums[r] > nums[l]:
                nums[r], nums[l+1] = nums[l+1], nums[r]
                l += 1
            r += 1
            
        return l + 1