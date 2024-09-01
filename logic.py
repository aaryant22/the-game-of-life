def get_next_state(grid):
    n = len(grid)
    m = len(grid[0])
    new_grid = [[0]*m for _ in range(n)]

    def count_alive_neighbors(i,j):

        count=0
        directions=[(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]
        for x,y in directions:
            current_x, current_y = i+x,j+y
            if 0 <= current_x < n and 0 <= current_y < m:
                if grid[current_x][current_y] == 1:
                    count+=1
        
        return count
    
    for i in range(n):
        for j in range(m):
            live_neighbors = count_alive_neighbors(i, j)
            if grid[i][j] == 0 and live_neighbors==3:
                new_grid[i][j] = 1
            elif grid[i][j] == 1 and (live_neighbors<2 or live_neighbors>3):
                new_grid[i][j] = 0
            else:
                new_grid[i][j] = grid[i][j]
            
    return new_grid
