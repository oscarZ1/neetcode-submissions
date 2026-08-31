class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = defaultdict(int) 
        for n in nums: 
            res[n] += 1
        
        output = []
        for i in range(k): 
            key, value = max(res.items(), key=lambda kv: kv[1])
            output.append(key)
            res.pop(key, None) 
        
        return output