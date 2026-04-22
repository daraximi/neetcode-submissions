class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        p1 , p2 = 0 , 0
        minima = (min(len(word1), len(word2))) 
        res = ""

        while p1 < minima and p2 < minima:
            res += (word1[p1])
            p1 += 1
            res += (word2[p2])
            p2 += 1
        if p1:
            res += (word1[p1:])

        if p2:
            res += (word2[p2:])

        return res