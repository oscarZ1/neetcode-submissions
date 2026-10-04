class Solution:
    def isValid(self, s: str) -> bool:
        stack = [] 
        
        for c in s: 
            if (c == '}' or c == ')' or c == ']') and len(stack) == 0: 
                return False 
            
            if c == ')':
                if stack.pop() != '(': 
                    return False 
            elif c == '}': 
                if stack.pop() != '{': 
                    return False 
            elif c == ']': 
                if stack.pop() != '[':
                    return False     
            else: 
                stack.append(c) 
        
        return len(stack) == 0