import heapq

def minEffort(puzzle):

    # declare a graph to store the absolute distance between nodes
    graph = {}

    # loop through each row of puzzle
    for x in range(len(puzzle)):

        # loop through each column of puzzle for row x
        for y in range(len(puzzle[x])):

            # create a temp dictionary to store the vertices with the absoluter length
            temp_dict = {}

            # get the absolute value of below node
            if x+1 < len(puzzle):
                temp_dict['{},{}'.format(x+1,y)] = abs(puzzle[x+1][y] - puzzle[x][y])
            # get the absolute value of above node
            if x-1 >= 0:
                temp_dict['{},{}'.format(x-1,y)] = abs(puzzle[x-1][y] - puzzle[x][y])
            # get the absolute value of right node
            if y+1 < len(puzzle[x]):
                temp_dict['{},{}'.format(x,y+1)] = abs(puzzle[x][y+1] - puzzle[x][y])
            # get the absolute value of left node
            if y-1 >= 0:
                temp_dict['{},{}'.format(x,y-1)] = abs(puzzle[x][y-1] - puzzle[x][y])

            # append the vertices connect to xy to the graph dictionary
            graph['{},{}'.format(x,y)] = temp_dict

    # get the path distances for each node from starting vertex by minimal effort
    distances = dijkstra(graph,'0,0')

    # return the n-1, m-1 from dictionary
    return distances['{},{}'.format(x,y)]

def dijkstra(graph,starting_vertex):

    # declare all vertices as infinity and set the starting vertex to 0
    distances = {vertex: float('infinity') for vertex in graph}
    distances[starting_vertex] = 0

    # create a priority queue with heap queue to properly track movement
    pq = [(0, starting_vertex)]

    # iterate through the pq until it is empty
    while len(pq) > 0:
        current_distance, current_vertex = heapq.heappop(pq)

        # Nodes can get added to the priority queue multiple times. We only
        # process a vertex the first time we remove it from the priority queue.
        if current_distance > distances[current_vertex]:
            continue

        # process the neighbors
        for neighbor, weight in graph[current_vertex].items():

            # since we are only interested in the minimal effort we can store the max between the current distance
            # and weight
            distance = max(current_distance,weight)

            # Only consider this new path if it's better than any path we've
            # already found.
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(pq, (distance, neighbor))

    # return the paths
    return distances

if __name__ == '__main__':
    puzzle = [[1, 1, 5, -50], [5, 8, 3, 1], [3, 4, 1, 4]]
    print(minEffort(puzzle))