class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        tracker = {}
        res = []
        for num in nums:
            tracker[num] = tracker.get(num, 0) + 1
        
        for i in range(k):
            curr_max = max(tracker, key=tracker.get)
            res.append(curr_max)
            del tracker[curr_max]
        
        return res



        