class Solution:
    def countSeniors(self, details: List[str]) -> int:
        res = 0
        def checker(detail):
            print(detail[:10])
            if len(detail) < 15:
                return False
            if detail[:10].isdigit():
                if int(detail[11:13]) > 60:
                    print(detail[11:13])
                    return True
                else:
                    
                    return False
            else:
                return False
            
        for s in details:
            if checker(s) == True:
                res = res + 1
        return res

        