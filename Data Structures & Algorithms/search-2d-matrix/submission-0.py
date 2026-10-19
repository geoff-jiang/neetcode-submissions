class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l, r = 0, len(matrix) - 1

        while l <= r: 
            mid = l + (r - l) // 2
            if target == matrix[mid][0]:
                return True
            elif target > matrix[mid][0] and target < matrix[r][0] or l == r:
                nl, nr = 0, len(matrix[mid]) - 1
                while nl <= nr:
                    nmid = nl + (nr - nl) // 2
                    if matrix[mid][nmid] == target:
                        return True
                    elif matrix[mid][nmid] > target:
                        nr = nmid - 1
                    else:
                        nl = nmid + 1
                return False
            elif target > matrix[mid][0]:
                l = mid + 1
            elif target < matrix[mid][0]:
                r = mid - 1
        return False
        