class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        longestLength = 0

        for num in numSet:
            length = 0

            if (num - 1) not in numSet:
                while (num + length) in numSet:
                    length += 1
            
            longestLength = max(longestLength, length)
        
        return longestLength