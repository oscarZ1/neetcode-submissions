class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indices = {} 
        
        for index, n in enumerate(nums): 
            indices[n] = index 
        
        for index, n in enumerate(nums): 
            diff = target - n 
            if diff in indices and index != indices[diff]: 
                return [index, indices[diff]] 
        
        return []