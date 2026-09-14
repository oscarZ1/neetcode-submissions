class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
            
        prefix = [0] * len(nums)
        postfix = [0] * len(nums)
        for i in range(len(nums)): 
            if i == 0: 
                prefix[i] = nums[i] 
            else: 
                prefix[i] = prefix[i-1] * nums[i]
        
        for i in range(len(nums)-1, -1, -1): 
            if i == len(nums)-1:
                postfix[i] = nums[i] 
            else: 
                postfix[i] = nums[i] * postfix[i+1]

        output = [0] * len(nums) 
        for i in range(len(output)): 
            if i == 0: 
                output[i] = postfix[i+1] 
            elif i == len(output) -1: 
                output[i] = prefix[i-1]
            else: 
                output[i] = prefix[i-1] * postfix[i+1]
        
        return output

        