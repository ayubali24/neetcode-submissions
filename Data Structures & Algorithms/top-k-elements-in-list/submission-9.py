class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}

        for num in nums:
            freq[num] = freq.get(num, 0) + 1
        
        buckets = [[] for i in range(len(nums) + 1)]

        for number, count in freq.items():
            buckets[count].append(number)
        
        res = []
        for i in range(len(buckets) - 1, -1, -1):
            for number in buckets[i]:
                res.append(number)
                if len(res) == k:
                    return res

        
