class Solution:
    def isHappy(self, n: int) -> bool:
        nstr = ""
        x = 0
        seen = []
        while n!=1:
            nstr = str(n)
            for i in nstr:
                x = x + int(i)**2
            n = x
            if n in seen:
                return False
            seen.append(n)
            x = 0
        return True
        
