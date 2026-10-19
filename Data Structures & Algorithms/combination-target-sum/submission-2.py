class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        def dfs(index, currentPath, total):
            if index >= len(nums) or total > target:
                return
            if total == target:
                res.append(currentPath.copy())
            else:
                currentPath.append(nums[index])
                dfs(index, currentPath, total + nums[index])
                currentPath.pop()
                dfs(index + 1, currentPath, total)

        dfs(0, [], 0)
        return res