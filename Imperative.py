import sys 
import itertools

NO_PATH =  999
"""
graph = [[0,   5,  NO_PATH, NO_PATH], 
         [50,  0,  15,  5], 
         [30, NO_PATH, 0,   15], 
         [15, NO_PATH, 5, 0]] 

graph1 = [[0, 3, NO_PATH, 5],
          [2, 0, NO_PATH, 4],
          [NO_PATH, 1, 0, NO_PATH],
          [NO_PATH, NO_PATH, 2, 0]]
"""
graph2 =[[0, NO_PATH, 3, NO_PATH,NO_PATH ],
[4, 0, NO_PATH, 1,2],
[3, 8, 0, 2,6],
[NO_PATH, 1, NO_PATH, 0,4],
[NO_PATH, 1, 6, 4,0]]


MAX_LENGTH = len(graph2[0]) 

def floyd(distance):  
    for intermediate, start_node, end_node in itertools.product (range(MAX_LENGTH),range(MAX_LENGTH), range(MAX_LENGTH)): 
            if start_node == end_node: 
                distance[start_node][end_node] = 0 
            else:
                distance[start_node][end_node] = min(distance[start_node][end_node], distance[start_node][intermediate] + distance[intermediate][end_node])
    print (distance) 
    
#floyd(graph)
#floyd(graph1)
floyd(graph2)

