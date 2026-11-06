from collections import defaultdict

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        lib = defaultdict(int)

        for i, v in enumerate(nums):
            if (target - v) in lib:
                return [lib[(target-v)], i]
            lib[v] = i
        return []