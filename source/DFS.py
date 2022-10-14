from numpy import true_divide

def check_in_matrix(matrix, point):
    if (point[0] < len(matrix) and point[0] >=0 and point[1] < len(matrix[0]) and point[1] >=0 and matrix[point[0]][point[1]] != 'x'):
        return True
    else:
        return False

def DFS(maze,start,end):
    visited, neighbor = [], []
    dirs=[(0, 1), (0, -1), (1, 0), (-1, 0)]

    trace = dict()
    trace[start] = None 
    visited.append(start)
    neighbor.append(start)
    curDirection =(1,0)

    while len(neighbor) != 0 :
        current = neighbor.pop()
        visited.append(current)

        if (current == end):
            break
        
        
        for step in dirs:
            next = (current[0] + curDirection[0], current[1] + curDirection[1])

            if (next not in visited) and check_in_matrix(maze, next):
                neighbor.append(next)  
                trace[next] = current
                curDirection = step
                #break
            else:
                curDirection = dirs[step+1]
                

    route = []
    check = end

    while check != start:
        route.append(check)
        check = trace[check]

    route.append(start)
    route.reverse()

    return route