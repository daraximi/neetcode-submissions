class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mymap  ={}
        for word in strs:
            lowerword = ''.join(sorted(word))
            if lowerword not in mymap:
                mymap[lowerword] = [word]
            else:
                mymap[lowerword].append(word)
        return list(mymap.values())
        