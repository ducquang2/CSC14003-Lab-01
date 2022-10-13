
from numpy import true_divide

def check_in_matrix(matrix, point):
    if (point[0] < len(matrix) and point[0] >=0 and point[1] < len(matrix[0]) and point[1] >=0 and matrix[point[0]][point[1]] != 'x'):
        return True
    else:
        return False

def DFS(maze,start,end):
    visited, neighbor = [], []
    dirs=[(0,1),(0,-1),(1,0),(-1,0)]

    trace = dict()
    trace[start] = None
    visited.append(start)
    neighbor.append(start)

    while len(neighbor) != 0:
        current = neighbor[-1]
        visited.append(current)
        neighbor.pop()

        if (current == end):
            break

        for step in dirs:
            next = (current[0] + step[0], current[1] + step[1])

            if check_in_matrix(maze, next):
                if next not in visited:
                    neighbor.append(next)
                    trace[next] = current
    route = []
    check = end

    while check != start:
        route.append(check)
        check = trace[check]

    route.append(start)
    route.reverse()

    return route
    # if start[0]==end[0] and start[1]==end[1]:
    #     return ((start[0],start[1]))
    # route = []    
    # dirs=[(0,1),(0,-1),(1,0),(-1,0)]
    # x,y = start[0],start[1]
    # for dx,dy in dirs:
    #     nx=x
    #     ny=y
    #     while 0 <= nx +dx < len(maze) and 0 <= ny +dy < len(maze) and maze[nx+dx][ny+dy] != 'x' :
    #         nx+=dx
    #         ny+=dy

    #     if maze[nx][ny] != 0:
    #         continue
            
    #     maze[nx][ny]=2

    #     if(DFS(maze,(nx,ny),end) == start):
    #         route.append((nx,ny))
    #         return route
    # return route


