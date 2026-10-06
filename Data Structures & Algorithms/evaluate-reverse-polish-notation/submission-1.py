class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = [] 
        for val in tokens: 
            if val == "+": 
                second, first = stack.pop(), stack.pop()
                stack.append(first+second)
            elif val == "-": 
                second, first = stack.pop(), stack.pop()
                stack.append(first - second)
            elif val == "*": 
                second, first = stack.pop(), stack.pop()
                stack.append(first * second) 
            elif val == "/": 
                second, first = stack.pop(), stack.pop()
                stack.append(int(float(first) / second))
            else: 
                stack.append(int(val))
                
            
        return stack[0]