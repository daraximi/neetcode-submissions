class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        if len(nums) == 1:
            return nums
        center = len(nums) // 2
        left = self.sortArray(nums[:center])
        right = self.sortArray(nums[center:])

        def merge(left, right):
            results = []
            i = j = 0
            while (i < len(left) and j < len(right)):
                if(left[i] < right[j]):
                    results.append(left[i])
                    i += 1
                else:
                    results.append(right[j])
                    j += 1
            return results + left[i:] + right[j:]




        return merge(left, right)
        