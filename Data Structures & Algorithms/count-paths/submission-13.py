class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        oldRow = [1] * n
        
        for i in range(m - 2, -1, -1):
            newRow = [0] * n
            rightValue = 1
            for j in range(n - 2, -1, -1):
                newRow[j] = rightValue + oldRow[j]
                rightValue = newRow[j]
            oldRow = newRow
        
        return oldRow[0]

        
        # row = [1] * n

        # for i in range(m - 1):
        #     current_row = [1] * n
        #     for j in range(n-2, -1, -1):
        #         current_row[j] = current_row[j + 1] + row[j]
        #     row = current_row
        # return row[0]

        #TC = O(n * m) = SC
        # TC = O(n * m) , SC + O(n + m)
        





                





