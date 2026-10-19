class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        x = len(digits)-1
        while x>=0:
            if digits[x]==9:
                digits[x] = 0
                x = x-1
            else:
                digits[x] = digits[x]+1
                return digits
        if digits[0]==0:
            digits.insert(0,1)
            return digits
        else:
            return digits