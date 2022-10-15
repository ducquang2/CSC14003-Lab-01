from collections import deque

def check_in_matrix(matrix, point):
    if (point[0] < len(matrix) and point[0] >=0 and point[1] < len(matrix[0]) and point[1] >=0 and matrix[point[0]][point[1]] != 'x'):
        return True
    else:
        return False

def BFS(matrix, start, end, bonus_points):
    path = deque()
    path.append(start)
    visited = []
    trace = dict()
    trace[start] = None
    dicrections = [[0, 1], [0, -1], [1, 0], [-1, 0]]
    current=(0,0)

    while len(path) != 0:
        current = path.popleft()

        if (current == end): break # Chi out khi gap diem ket thuc

        for dir in dicrections:
            point = (current[0] + dir[0], current[1] + dir[1])

            if check_in_matrix(matrix=matrix, point= point) and point not in visited:
                trace[point] = current
                path.append(point)
                visited.append(point)

    if(current!=end):
        return None,-1
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
    return route, cost     