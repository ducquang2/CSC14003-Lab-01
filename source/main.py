import sys, getopt
from implement import *
from BFS import *
from DFS import *
from UCS import *
from GBFS import *
from A_SAO import *

# PATH = './input/level_2/input3.txt'

def main(argv):
    in_file, out_file = './input/', ''
    try:
        opts, argv = getopt.getopt(argv, 'hi:o', ['input=', 'output='])
    except getopt.GetoptError:
        print('Error command')
        sys.exit(2)

    for opt, arg in opts:
        if opt == '--in':
            in_file += arg
        elif opt == '--out':
            out_file += arg

    bonus_points, matrix = read_file(in_file)
    start, end = getStartEndPoint(matrix)
    
    # out_put = './output/BFS.jpg'
    route,explored,cost = BFS(matrix,start,end,bonus_points)
    write_cost_path(cost)
    visualize_maze(matrix,bonus_points,start,end,out_file,route,explored)

    # out_put = './output/DFS.jpg'
    route,explored,cost = DFS(matrix,start,end,bonus_points)
    write_cost_path(cost)
    visualize_maze(matrix,bonus_points,start,end,out_file,route,explored)

    # out_put = './output/UCS.jpg'
    route,explored,cost = UCS(matrix,start,end,bonus_points)
    write_cost_path(cost)
    visualize_maze(matrix,bonus_points,start,end,out_file,route,explored)

    # out_put = './output/GBFS.jpg'
    route,explored,cost = GBFS(matrix,start,end,bonus_points)
    write_cost_path(cost)
    visualize_maze(matrix,bonus_points,start,end,out_file,route,explored)

    # out_put = './output/AStar.jpg'
    route,explored,cost = AStar(matrix,start,end,bonus_points)
    write_cost_path(cost)
    visualize_maze(matrix,bonus_points,start,end,out_file,route,explored)

if __name__ == '__main__':
    main()
