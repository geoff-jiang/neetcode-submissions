class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # a set which stores value and the index it is at. each number search the set
        # {2: 1
            # 1 : 2} 
        store = defaultdict(int)
        for i, v in enumerate(numbers): 
            if v in store:
                return [store[v], i + 1]
            store[target - v] = i + 1
        
