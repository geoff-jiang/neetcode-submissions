class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        ROWS = len(board)
        COLS = len(board[0])
        DIRECTIONS = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        visited = set()
        def dfs(point, index):
            if point in visited:
                return False
            if index == len(word):
                return True
            cx, cy = point
            
            visited.add(point)
            for x, y in DIRECTIONS: 
                nx = x + cx
                ny = y + cy
                if 0 <= nx < ROWS and 0 <= ny < COLS and board[nx][ny] == word[index]:
                    if dfs((nx, ny), index + 1):
                        return True
            
            visited.remove(point)
            return False

        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == word[0]:
                    if dfs((r, c), 1):
                        return True
        
        return False
            