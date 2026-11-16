class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = []
        freqCounter = {}
        tracker = [[] for i in range(len(nums)+1)]

        for num in nums:
            freqCounter[num] = freqCounter.get(num, 0) + 1
        
        for num, count in freqCounter.items():
            tracker[count].append(num)
  
        
        for i in range(len(tracker) -1, -1, -1):
            for num in tracker[i]:
                res.append(num)
                if len(res) == k:
                    return res
            
