# Author: Timur Guner
# Class: CS325
# Term: Winter 2021
# Assignment: Assignment 9 TSP

def solve_tsp(G):

    # create a size variable and a track of cost
    cost = 0
    size = len(G)
    start = 0

    # create a set of visited nodes
    visited = set()
    visited.add(0)
    path = []
    path.append(0)

    # go through each row of the matrix except for the final visited row in the matrix
    # find the min cost to the adjacent nodes in the row that were not visited
    # save the min cost for the current adjacent node walk and proceed to that node that corresponds to the row
    for x in range(0,size-1):
        min = float("inf")
        for y in range(0,size):
            if start != y and G[start][y] < min and y not in visited and G[start][y] != 0:
                min = G[start][y]
                index = y
        visited.add(index)
        path.append(index)
        start = index
        cost += min

    # add the cost of last node visited to starting node
    cost += G[start][0]

    return path

if __name__ == '__main__':
    G = [
    [0, 0, 3, 20, 1],
    [0, 0, 15, 2, 20],
    [3, 15, 0, 20, 13],
    [20, 2, 20, 0, 9],
    [1, 20, 13, 9, 0]]

    print(solve_tsp(G))
