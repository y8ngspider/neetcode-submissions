class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        stack = []
        operator = ('+','-','*','/')
        res=0
        if len(tokens)==1 and tokens[0] not in operator:
            return int(tokens[0])
        for n in tokens:
            print(stack)
            if n not in operator:
                #push numbers onto stack
                stack.append(int(n))
            else:
                n1 = stack.pop()
                n2 = stack.pop()
                if n == '+':
                    res = n2 + n1
                elif n == '-':
                    res = n2 - n1
                elif n == '*':
                    res = n2 * n1
                elif n == '/':
                    res = int(n2 / n1)
                print(res)
                stack.append(res)
        return res
                    
