class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if not nums:
            return nums

        max_val = max(nums)
        count = [0] * (max_val+1)

        for num in nums:
            count[num] += 1
        
        idx = 0
        for value in range(len(count)):
            while count[value] > 0:
                nums[idx] = value
                idx += 1
                count[value] -= 1