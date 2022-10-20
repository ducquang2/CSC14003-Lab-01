from numpy import true_divide

def check_in_matrix(matrix, point):
    if (point[0] < len(matrix) and point[0] >=0 and point[1] < len(matrix[0]) and point[1] >=0 and matrix[point[0]][point[1]] != 'x'):
        return True
    else:
        return False

def DFS(maze,start,end,bonus_points):
    frontier, explored = [], []
    dirs=[(0, 1), (1, 0), (-1, 0), (0,-1)] #right down up left

    trace = dict()
    trace[start] = None 
    frontier.append(start)
    explored.append(start)
    preDirection =(0,0)
    temp=(0,0)
    while len(frontier) != 0 :
        current = frontier.pop()

        if (current == end):
            route = []
            check = end
            while check != start:
                route.append(check)
                check = trace[check]
            route.append(start)
            route.reverse()
            cost = len(route)
            for bp in bonus_points:
                if (bp[0],bp[1]) in route:
                    cost = cost + bp[2]
            return route,explored,cost     
        
        for step in dirs:
            next = (current[0] + step[0], current[1] + step[1])
            if next not in explored and check_in_matrix(maze, next) and step!=preDirection:
                explored.append(next) 
                frontier.append(next)
                trace[next] = current
                temp=step

        nextNow = (current[0] + preDirection[0], current[1] + preDirection[1])
        if nextNow not in explored and check_in_matrix(maze, nextNow):
                explored.append(nextNow) 
                frontier.append(nextNow)
                trace[nextNow] = current
        else:
            preDirection=temp
                
    return None,None,-1