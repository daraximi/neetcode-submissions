class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n = len(nums) // 3
        myMap = {}
        res = []
        for num in nums:
            myMap[num] = myMap.get(num, 0) + 1
        
        for key,value in myMap.items():
            if (value > n):
                res.append(key)
        return res
