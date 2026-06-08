class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []

        def backtrack(current, i):
            if i > n:
                if len(current) == k:
                    res.append(current.copy())
                return
            current.append(i)
            backtrack(current, i + 1)
            current.pop()
            backtrack(current, i + 1)
        backtrack([], 1)
        return res