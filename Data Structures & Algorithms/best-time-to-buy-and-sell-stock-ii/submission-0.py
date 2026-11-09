class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        stack = []
        profit = 0
        for i in range(len(prices)):
            if stack and stack[-1] > prices[i]:
                if len(stack)>1:
                    profit += -stack[0] + stack[-1]
                stack = []
            stack.append(prices[i])
        if stack and len(stack) > 1:
            profit += -stack[0] + stack[-1]
        return profit
