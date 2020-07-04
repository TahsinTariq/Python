from collections import deque
import heapq

parents = {}
cost = {}

def rout(v1,v2):
    if v1 == v2:
        print(v1)
        print(0)
        return None
    else:
        try:
            s = 0
            route(v1,v2)
            c = cost[v2] - cost[v1]
            if c > -1:
                print('cost :', c,'\n')
        except Exception as e:
            print('No path exists')

def route(v1, v2):
    if parents[v2] != v1:
        route(v1, parents[v2])
    print(v2)


def DJ(hash_, v1, v2):
    queue = deque()
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
                        parents[n] = d1
                print("\t\tParents: \n\t\t", parents, "\n\t\tCost:\n\t\t", cost, "\n")

    while queue:
        # print("Queue: \n", queue)
        node = queue.popleft()
        lowestCost(node)
        searched.append(node)
        # print("Searched: \n", searched)


if __name__ == '__main__':
    # HASH = {'e': {'r': 2, 'h': 8}, 'r': {'f': 1}, 'G': {}, 'c': {'a': 2}, 'q': {}, 'h': {'p': 1, 'q': 1},
    #         'f': {'G': 2, 'c': 1}, 'd': {'e': 2, 'c': 8, 'b': 1}, 'S': {'e': 9, 'd': 3, 'p': 1}, 'p': {'q': 15},
    #         'a': {'G':1}, 'b': {'a': 2}}
    # DJ(HASH, 'S', 'G')

    HASH = {'A': {'B': 4, 'C': 3, 'D': 20},
             'B': {'E': 1},
             'C': {'E': 22},
             'D': {'E': 7},
             'E': {}}
    DJ(HASH, 'A', 'E')

    for i in HASH:
        for j in HASH:
            print("From ", i, " to ", j, ":")
            rout(i,j)
            print("\n")