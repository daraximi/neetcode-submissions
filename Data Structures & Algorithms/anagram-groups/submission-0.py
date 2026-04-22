class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = []
        myMap = {}

        for currStr in strs:
            trs = tuple(sorted(currStr))
            if trs in myMap:
                myMap[trs].append(currStr)
            else:
                myMap[trs] = [currStr]
        for key, val in myMap.items():
            res.append(val)
        return res
        
        