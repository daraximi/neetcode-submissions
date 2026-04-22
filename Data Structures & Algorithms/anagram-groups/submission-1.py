class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if strs is None:
            return None
        resultMap = {}
        for string in strs:
            if ''.join(sorted(string)) not in resultMap:
                resultMap[''.join(sorted(string))] = [string]
            else:
                resultMap[''.join(sorted(string))].append(string)
        resultArray = []
        for key in resultMap:
            resultArray.append(resultMap[key])
        return resultArray
        