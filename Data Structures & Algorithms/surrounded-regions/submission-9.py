class Solution:
    def solve(self, board: List[List[str]]) -> None:
        # BFS when we encounter an O, keep a flag if the region touches the boundary
        # if finish and flag is false, backtrack and mark all O's as X's? 
        # keep path as an array of points?just use the visited set? 


        ROWS = len(board)
        COLS = len(board[0])
        DIRECTIONS = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        visited = set()

        def bfs(r, c): 
            queue = deque([(r, c)])
            isRegion = True
            currentVisited = set()

            while queue:
                cr, cc = queue.popleft()
                if (cr, cc) in currentVisited or (cr, cc) in visited:
                    continue
                if (cr == 0 or cr == ROWS - 1 or cc == 0 or cc == COLS - 1):
                    isRegion = False    

                visited.add((cr, cc))
                currentVisited.add((cr, cc))
                for x, y in DIRECTIONS:
                    nx = cr + x
                    ny = cc + y
                    if 0 <= nx < ROWS and 0 <= ny < COLS and board[nx][ny] == "O":
                        queue.append((nx, ny))
            if isRegion:
                for x, y in currentVisited:
                    if board[x][y] == "O":
                        board[x][y] = "X"



        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == "O" and (r, c) not in visited: 
                    bfs(r, c)
            

        
        

