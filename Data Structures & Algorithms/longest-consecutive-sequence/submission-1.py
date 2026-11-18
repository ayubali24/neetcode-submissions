class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numsSet = set(nums)

        longest = 0

        for num in numsSet:
            length = 0
            if (num-1) in numsSet:
                continue
            start = num
            length = 1
            while (start+1) in numsSet:
                length += 1
                start+=1
            longest = max(longest, length)
        
        return longest