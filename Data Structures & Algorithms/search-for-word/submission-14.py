class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS = len(board)
        COLS = len(board[0])

        DIRECTIONS = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        visited = set()

        def dfs(r, c, i):
            if not(0 <= r < ROWS and 0 <= c < COLS) or (r, c) in visited or board[r][c] != word[i]:
                return False
            if i == len(word) - 1:
                return True
            visited.add((r, c))

            for x, y in DIRECTIONS:
                nx = x + r
                ny = y + c
                if dfs(nx, ny, i + 1):
                    return True
            visited.remove((r, c))
            return False

        for r in range(ROWS):
            for c in range(COLS):
                    if dfs(r, c, 0):
                        return True
        
        return False