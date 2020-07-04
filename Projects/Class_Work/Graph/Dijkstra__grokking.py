from collections import deque
import heapq
parents = {}
cost = {}
hash_ = {}

def rout(v1,v2):
    if v1 == v2:
        print(v1)
        print(0)
        return None
    else:
        try:
            print(v1)
            route(v1,v2)
            c = cost[v2] - cost[v1]
            if c > -1:
                print('cost :', c,'\n')
        except Exception as e:
            print('No path exists')


def route(v1, v2):
    if parents[v2] != v1:
        # if hash_[v1][parents[v2]]:
        # print(hash_[v2])
        route(v1, parents[v2])
        print(v2)
    else:
        print(v2)

def DX(table, v1):
    queue = deque()
    def MakeHash():
#DO NOT, UNDER ANY CIRCUMSTANCES,CHANGE THIS PARTICULAR LINE OF CODE.THE ENTIRE FATE OF THIS ALGORITHM DEPENDS ON THIS#
        for i in table[0][1:]:
            hash_[i] = dict((table[0][j+1],x) for j, x in enumerate(table[table[0].index(i)][1:]) if int(x) > 0)
                                        ############################
        # print(hash_)
    MakeHash()
    for i in hash_.keys():
        cost[i] = float('inf')
    queue += [v1]
    parents[v1] = "NONE"
    cost[v1] = 0
    searched = []
    def lowestCost(d1):
        val = [hash_[d1][j]for j in hash_[d1]]
        heapq.heapify(val)
        while val:
            v = heapq.heappop(val)
            for city, x in hash_[d1].items():
                if x == v:
                    if city not in searched:
                        queue.append(city)
                    if x+cost[d1] < cost[city]:
                        cost[city] = x+cost[d1]
                        parents[city] = d1
                    print("Parents: \n",parents,"\nCost:\n",cost,"\nSearched: \n",searched,"\n")

    while queue:
        node = queue.popleft()
        lowestCost(node)
        searched.append(node)
        # print("\n\nQueue: ", queue)
    # rout(v1,v2)

if __name__ == '__main__':
    a = [['n/a', 'Atlanta', 'Austin', 'Chicago', 'Dallas', 'Denver', 'Houston', 'Boston'],
         ['Atlanta', 0, 0, 0, 0, 0, 800, 600],
         ['Austin', 0, 0, 0, 20, 0, 160, 0],
         ['Chicago', 0, 0, 0, 0, 1000, 0, 0],
         ['Dallas', 0, 200, 900, 0, 780, 0, 888],
         ['Denver', 40, 0, 1000, 0, 0, 0, 0],
         ['Houston', 800, 0, 0, 0, 0, 0, 0],
         ['Boston', 600, 0, 0, 1300, 0, 0, 0]]
    DX(a, "Austin", "Atlanta")