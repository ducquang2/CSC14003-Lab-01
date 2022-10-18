from queue import PriorityQueue
from BFS import check_in_matrix

def UCS(matrix, start, end, bonus_points):    
    waiting = PriorityQueue()
    waiting.put(start, 0)
    directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]

    trace, cost = {}, {}
    trace[start], cost[start] = None, 0

    while not waiting.empty():
        current = waiting.get()

        if (current == end):
            route = []
            routeall = []
            check = end
            while check != start:
                route.append(check)
                check = trace[check]
            route.append(start)
            route.reverse()
            
            cost_val = cost[end]
            for bp in bonus_points:
                if (bp[0],bp[1]) in route:
                    cost_val = cost_val + bp[2]
            for key in trace.keys():
                routeall.append(key)
            return route, routeall, cost_val
        
        for step in directions:
            point = (current[0] + step[0], current[1] + step[1])

            if not check_in_matrix(matrix, point):
                continue

            next_cost = cost[current] + 1 # chi phi moi buoc deu la 1

            if (point not in cost) or (next_cost < cost[point]):
                cost[point] = next_cost
                waiting.put(point, next_cost)
                trace[point] = current

    return None,None,-1