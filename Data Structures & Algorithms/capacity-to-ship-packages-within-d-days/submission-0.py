class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        n = len(weights)
        l = max(weights)
        r = sum(weights)
        res = r
        while l <= r:
            capacity = (l + r) // 2
            curr_days = 1
            curr_sum = 0
            for w in weights:
                if curr_sum + w > capacity:
                    curr_days += 1
                    curr_sum = w
                else:
                    curr_sum += w
            if curr_days <= days:
                res = capacity
                r = capacity - 1
            else:
                l = capacity + 1
        return res