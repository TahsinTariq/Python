def dijkstra(graph, start, end):
    shortest_distance = {}
    predecssor = {}
    unseenNodes = graph.copy()
    infinity = 99999
    path = []
    predecssor[start] = None

    for node in unseenNodes:
        shortest_distance[node] = infinity
        shortest_distance[start] = 0

    while unseenNodes:
        min_distance_node = None

        for node in unseenNodes:
            if min_distance_node is None:
                min_distance_node = node
            elif shortest_distance[node] < shortest_distance[min_distance_node]:
                min_distance_node = node

        path_options = graph[min_distance_node].items()

        for child_node, weight in path_options:
            if weight + shortest_distance[min_distance_node] < shortest_distance[child_node]:
                shortest_distance[child_node] = weight + shortest_distance[min_distance_node]
                predecssor[child_node] = min_distance_node

        unseenNodes.pop(min_distance_node)
    currentNode = end

    while currentNode != start:
        try:
            path.insert(0, currentNode)
            currentNode = predecssor[currentNode]
        except KeyError:
            print('path not exists')
            break
    path.insert(0, start)

    if shortest_distance != infinity:
        print('shortest distance is ' + str(shortest_distance[end]))
        print('optimal path is ' + str(path))

if __name__ == '__main__':

    graph = {'A': {'B': 4, 'C': 3, 'D': 20},
             'B': {'D': 3, 'E': 1},
             'C': {'B': 6, 'D': 43, 'E': 22},
             'D': {'E': 7},
             'E': {}}
    for i in graph:
        for j in graph:
            print("From ", i, " to ", j, ":")
            dijkstra(graph,i, j)
