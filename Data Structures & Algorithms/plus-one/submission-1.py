class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        if digits[-1] < 9:
            digits[-1]+=1
            return digits
        
        j = len(digits)-1
        while digits[j] == 9 and j >= 0:
            print(j)
            digits[j]=0
            j-=1
        
        if j >= 0:
            digits[j] += 1
        else:
            digits.insert(0,1)
        return digits
