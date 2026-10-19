class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # dfs, dict of (point, uniquepaths), visited set to track cycles
        # after last dfs finishes, return dict[end]

        # dp = [[0] * (n + 1) for i in range(m + 1)]

        # dp[m - 1][n-1] = 1
        
        row = [1] * n

        for i in range(m - 1):
            current_row = [1] * n
            for j in range(n-2, -1, -1):
                current_row[j] = current_row[j + 1] + row[j]
            row = current_row
        return row[0]

        #TC = O(n * m) = SC
        # TC = O(n * m) , SC + O(n + m)
        





                





