class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        my_dict = {}
        res = [[] for i in range(len(nums) + 1)]
        answer = []
        for num in nums:
            my_dict[num] = my_dict.get(num, 0) + 1
        
        for key, value in my_dict.items():
            res[value].append(key)

        for i in range(len(nums), -1, -1):
            for num in res[i]:
                answer.append(num)
                if len(answer) == k:
                    return answer

        print(my_dict)
        print(res)
        print(len(res))
        return []