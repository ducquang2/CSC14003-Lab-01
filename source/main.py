from implement import *
from BFS import *
from DFS import *
from UCS import *

def main():
    bonus_points, matrix = read_file(PATH)
    print(f'The height of the matrix: {len(matrix)}')
    print(f'The width of the matrix: {len(matrix[0])}')
    start, end = getStartEndPoint(matrix)
    print(matrix, bonus_points, start, end)
    route,explored,cost = UCS(matrix,start,end,bonus_points)
    write_cost_path(cost)
    visualize_maze(matrix,bonus_points,start,end,route,explored)
    
if __name__ == '__main__':
    main()
