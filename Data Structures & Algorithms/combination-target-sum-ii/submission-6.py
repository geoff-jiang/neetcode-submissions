class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()

        res = []
        def dfs(index, currentPath, total):
            if total == target:
                res.append(currentPath.copy())
                return
            if index >= len(candidates) or total > target:
                return
            currentPath.append(candidates[index])
            dfs(index + 1, currentPath, total + candidates[index])
            currentPath.pop()
            while index < len(candidates) - 1 and candidates[index + 1] == candidates[index]:
                index += 1
            dfs(index + 1, currentPath, total)

        dfs(0, [], 0)
        return res

