from collections import deque


def check_in_matrix(matrix, point):
    if (point[0] < len(matrix) and point[0] >=0 and point[1] < len(matrix[0]) and point[1] >=0 and matrix[point[0]][point[1]] != 'x'):
        return True
    else:
        return False
    
def is_bonus_point(point, bonus_points):
    for bp in bonus_points:
        if point[0]==bp[0] and point[1]==bp[1]:
            return True, bp[2]
    return False,0

def UCS(maze,start,end,bonus_points):
    explored = []
    frontier = deque()
    dirs=[(0, 1), (1, 0), (-1, 0), (0,-1)] #right down up left
    
    trace = dict()
    trace[start] = None 
    frontier.append(start)
    explored.append(start)

    cost=0
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
            cost = cost+ len(route)
            return route, cost     
        temp=(0,0)
        for step in dirs:
            next = (current[0] + step[0], current[1] + step[1])
            if next not in explored and check_in_matrix(maze, next):
                isBp,value = is_bonus_point(next, bonus_points)
                if(isBp):
                    temp=next
                    cost=cost+value
                else:
                    explored.append(next) 
                    frontier.append(next)
                    trace[next] = current
        explored.append(temp) 
        frontier.append(temp)
        trace[temp] = current
                    
    return None,-1