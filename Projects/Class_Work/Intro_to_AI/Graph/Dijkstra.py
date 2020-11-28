from collections import deque
import heapq


def DJ(hash_, v1, v2):
    parents = {}
    cost = {}
    queue = deque()

    def route(v1, v2):
        if parents[v2] != parents[v1]:
            route(v1, parents[v2])
        print(v2)

    for i in hash_.keys():
        cost[i] = float('inf')
    queue += [v1]
    parents[v1] = "NONE"
    cost[v1] = 0
    searched = []

    def lowestCost(d1):
        val = [hash_[d1][j] for j in hash_[d1]]
        heapq.heapify(val)
        while val:
            v = heapq.heappop(val)
            for n, c in hash_[d1].items():
                if c == v:
                    if n not in searched:
                        queue.append(n)
                    if c + cost[d1] < cost[n]:
                        cost[n] = c + cost[d1]
                        parents[n] = d1  # print("\t\tParents: \n\t\t", parents, "\n\t\tCost:\n\t\t", cost, "\n")

    while queue:  # print("Queue: \n", queue)
        node = queue.popleft()
        lowestCost(node)
        searched.append(node)  # print("Searched: \n", searched)
    try:
        route(v1, v2)
        print(cost[v2])
    except Exception as e:
        print('No path exists')


if __name__ == '__main__':
    HASH = {'e': {'r': 2, 'h': 8}, 'r': {'f': 1}, 'G': {}, 'c': {'a': 2}, 'q': {}, 'h': {'p': 1, 'q': 1},
            'f': {'G': 2, 'c': 1}, 'd': {'e': 2, 'c': 8, 'b': 1}, 'S': {'e': 9, 'd': 3, 'p': 1}, 'p': {'q': 15},
            'a': {}, 'b': {'a': 2}}
    DJ(HASH, 'S', 'G')
