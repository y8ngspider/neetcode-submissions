class Solution:
    def isValid(self, s: str) -> bool:
        check = []
        left = ['(','[','{']
        right = [')','}',']']
        for i in range (len(s)):
            ch = s[i]
            if(ch in left):
                check.append(ch)
            elif (ch in right):
                if (len(check)==0):
                    return False
                elif(ch==']'):
                    if (check[-1]!='['):
                        return False
                    check.pop()
                elif(ch=='}'):
                    if (check[-1]!='{'):
                        return False
                    check.pop()
                elif(ch==')'):
                    if (check[-1]!='('):
                        return False
                    check.pop()
        if (len(check)!=0):
            return False
        return True