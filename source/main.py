from implement import *
from BFS import *
from DFS import *
from UCS import *
from GBFS import *
from A_SAO import *

PATH = './input/map2.txt'

def main():
    bonus_points, matrix = read_file(PATH)
    # print(f'The height of the matrix: {len(matrix)}')
    # print(f'The width of the matrix: {len(matrix[0])}')
    start, end = getStartEndPoint(matrix)
    # print(matrix, bonus_points, start, end)
    out_put = './output/BFS.jpg'
    route,explored,cost = BFS(matrix,start,end,bonus_points)
    write_cost_path(cost)
    visualize_maze(matrix,bonus_points,start,end,out_put,route,explored)

    out_put = './output/DFS.jpg'
    route,explored,cost = DFS(matrix,start,end,bonus_points)
    write_cost_path(cost)
    visualize_maze(matrix,bonus_points,start,end,out_put,route,explored)

    out_put = './output/UCS.jpg'
    route,explored,cost = UCS(matrix,start,end,bonus_points)
    write_cost_path(cost)
    visualize_maze(matrix,bonus_points,start,end,out_put,route,explored)

    out_put = './output/GBFS.jpg'
    route,explored,cost = GBFS(matrix,start,end,bonus_points)
    write_cost_path(cost)
    visualize_maze(matrix,bonus_points,start,end,out_put,route,explored)

    out_put = './output/AStar.jpg'
    route,explored,cost = AStar(matrix,start,end,bonus_points)
    write_cost_path(cost)
    visualize_maze(matrix,bonus_points,start,end,out_put,route,explored)

if __name__ == '__main__':
    main()
