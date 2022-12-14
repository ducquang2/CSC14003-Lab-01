from queue import PriorityQueue
from BFS import check_in_matrix

def UCS(matrix, start, end, bonus_points):    
    waiting = PriorityQueue()
    waiting.put((0, start))
    visited = []
    bp_dict = dict()
    directions = [(0, 1), (1, 0), (-1, 0), (0,-1)]
    for x, y, b in bonus_points:
        if (x, y) not in bp_dict:
            bp_dict[(x, y)] = b

    trace, cost = {}, {}
    trace[start], cost[start] = None, 0

    while not waiting.empty():
        current = waiting.get()[1]

        if (current == end):
            route = []
            check = end
            cost_val = 0
            total_bonuses = 0

            while check != start:
                route.append(check)
                cost_val += 1
                if check in bp_dict:
                    total_bonuses += bp_dict[check]
                    cost_val += bp_dict[check]
                    print(check)
                check = trace[check]

            cost_val = 0 if cost_val < 0 else cost_val
            print('Total bonuses:', total_bonuses)
            print('Total cost:', cost_val)

            route.append(start)
            route.reverse()
            
            return route, visited, cost_val
        
        for step in directions:
            point = (current[0] + step[0], current[1] + step[1])

            if not check_in_matrix(matrix, point):
                continue

            next_cost = cost[current]

            if point in bp_dict:
                next_cost += bp_dict[point]

            next_cost += 1

            if ((point not in cost) or (next_cost < cost[point])) and (point not in visited):
                cost[point] = next_cost
                waiting.put((next_cost, point))
                visited.append(point)
                trace[point] = current

    return None,None,-1