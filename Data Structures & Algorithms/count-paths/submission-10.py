class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[1] * n for i in range(m)]

        for i in range(m - 2, -1, -1):
            for j in range(n - 2, -1, -1):
                dp[i][j] = dp[i + 1][j] + dp[i][j + 1]
        
        return dp[0][0]

        
        # row = [1] * n

        # for i in range(m - 1):
        #     current_row = [1] * n
        #     for j in range(n-2, -1, -1):
        #         current_row[j] = current_row[j + 1] + row[j]
        #     row = current_row
        # return row[0]

        #TC = O(n * m) = SC
        # TC = O(n * m) , SC + O(n + m)
        





                





