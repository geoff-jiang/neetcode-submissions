class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        # 1 2 3, target = 3
        # 1 -> (1, 1) , (1, 2)

        res = []

        def dfs(path, index, total):
            if index >= len(nums) or total > target:
                return
            
            if total == target:
                res.append(path.copy())
                return
            path.append(nums[index])
            dfs(path, index, total + nums[index])
            path.pop()
            dfs(path, index + 1, total)
            return
        
        dfs([], 0, 0)
        return res
