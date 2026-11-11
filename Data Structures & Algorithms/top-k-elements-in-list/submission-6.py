class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqCounter = {}

        for num in nums:
            freqCounter[num] = freqCounter.get(num, 0) + 1
        
        bucket = [[] for i in range(len(nums) +1)]

        for num, count in freqCounter.items():
            bucket[count].append(num)
        
        res = []
        for i in range(len(bucket) - 1, 0, -1):
            for num in bucket[i]:
                res.append(num)
                if len(res) == k:
                    return res

