from collections import deque

def solveMaze(maze):
    R, C = len(maze), len(maze[0])

    start = (0,0) 
    end = (0,0)
    for i in range(len(maze)):
        for j in range(len(maze[0])):
            if maze[i][j] == 'S':
                start=(i,j)

            elif maze[i][j] == ' ':
                if (i==0) or (i==len(maze)-1) or (j==0) or (j==len(maze[0])-1):
                    end = (i,j) 

            else:
                pass
    
    print(start,end)
    queue = deque()
    queue.appendleft((start[0], start[1], 0))
    directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
    visited = [[False] * C for _ in range(R)]
    wall = 'x'
    route = []
    temp = 0
    coord=(0,0,0)

    while len(queue) != 0:
        coord = queue.pop()
        route.append((coord[0],coord[1]))
        visited[coord[0]][coord[1]] = True
        
        
        if [coord[0]] == [end[0]] and [coord[1]] == [end[1]] : 
            return route   
        
        for dir in directions:
            nr, nc = coord[0]+dir[0], coord[1]+dir[1]
            if (nr < 0 or nr >= R or nc < 0 or nc >= C or maze[nr][nc] == wall or visited[nr][nc]): 
                continue
            queue.appendleft((nr, nc, coord[2]+1))

with open("./input/map_02.txt") as f:
    maze = []
    first_line = f.readline()
    for line in f:
        maze.append([i for i in line.strip("/n")])
    print((solveMaze(maze)))