class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        one = m -1
        two = n -1
        write = m + n - 1
        while two >= 0:
            if one >= 0 and nums1[one] >= nums2[two]:
                nums1[write] = nums1[one]
                one -= 1
            else:
                nums1[write] = nums2[two]
                two -= 1
            write -= 1