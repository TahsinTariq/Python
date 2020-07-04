import time

start_time = time.time()

def AStar(hash_, v1, v2, h):
    parents = {}
    gcost = {}
    fcost = {}
    queue = {}

    def route(v1, v2):
        if parents[v2] != parents[v1]:
            route(v1, parents[v2])
        print(v2)

    for i in hash_.keys():
        gcost[i] = float('inf')
        fcost[i] = float('inf')
    parents[v1] = "NONE"
    gcost[v1] = 0
    fcost[v1] = h[v1]
    queue[v1] = fcost[v1]

    def lowestCost(d1):
        for n, c in hash_[d1].items():
            if c + gcost[d1] < gcost[n]:
                gcost[n] = c + gcost[d1]
                fcost[n] = gcost[n] + h[n]
                parents[n] = d1
                if n not in queue.keys():
                    queue[n] = fcost[n]

    while queue:
        queue = {k: v for k, v in sorted(queue.items(), key=lambda item: item[1], reverse=True)}
        node, _ = queue.popitem()
        if node == v2:
            try:
                route(v1, v2)
                print(gcost[v2])
            except Exception as e:
                print('No path exists')
            return None
        print("\nsearching : ", node, " /\tfcost:", fcost[node])
        lowestCost(node)
    print("No          path          exists")


if __name__ == '__main__':
    HASH = {'Uri': {'Vaslui': 142, 'Hirosima': 98, 'Bucharest': 85},
            'Arad': {'Timisoara': 118, 'Zerind': 75, 'Sibiu': 140},
            'Bucharest': {'GUI': 90, 'Uri': 85, 'Pegasus': 211, 'Priest': 101}, 'Vaslui': {'Uri': 142, 'Lassi': 92},
            'Hirosima': {'Uri': 98, 'Eforie': 86}, 'Lassi': {'Vaslui': 92, 'Neamt': 87},
            'Lugoj': {'Mehedi': 70, 'Timisoara': 111}, 'GUI': {'Bucharest': 90}, 'Eforie': {'Hirosima': 86},
            'Craiova': {'Drobeta': 120, 'Priest': 138, 'Rimnicu': 146}, 'Zerind': {'Arad': 75, 'Oradea': 71},
            'Drobeta': {'Mehedi': 75, 'Craiova': 120}, 'Priest': {'Craiova': 138, 'Bucharest': 101, 'Rimnicu': 97},
            'Mehedi': {'Drobeta': 75, 'Lugoj': 70}, 'Neamt': {'Lassi': 97}, 'Timisoara': {'Arad': 118, 'Lugoj': 111},
            'Rimnicu': {'Craiova': 146, 'Priest': 97, 'Sibiu': 80}, 'Pegasus': {'Bucharest': 211, 'Sibiu': 90},
            'Oradea': {'Zerind': 71, 'Sibiu': 151}, 'Sibiu': {'Arad': 140, 'Pegasus': 99, 'Oradea': 151, 'Rimnicu': 80}}
    h = {'Eforie': 161, 'Mehedi': 241, 'Craiova': 160, 'Vaslui': 199, 'Priest': 100, 'Bucharest': 0, 'Hirosima': 151,
         'Zerind': 374, 'GUI': 77, 'Timisoara': 329, 'Sibiu': 253, 'Neamt': 234, 'Pegasus': 176, 'Lugoj': 244,
         'Rimnicu': 193, 'Lassi': 226, 'Drobeta': 242, 'Arad': 366, 'Oradea': 380, 'Uri': 80}

    AStar(HASH, "Arad", "Bucharest", h)
    print("--- %s seconds ---" % round(time.time() - start_time, 5))
