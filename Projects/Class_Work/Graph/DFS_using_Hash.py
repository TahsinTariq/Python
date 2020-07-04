from collections import deque


def BFS(table, v1, v2):
    ### MAKING HASH TABLE
    def duplicates(lst, item):
        return [i for i, x in enumerate(lst) if x == item]

    hash_ = {}
    parents = {}
    queue = deque()
    found = False

    def MakeHash():
        ind = 1
        for i in table[0][1:]:
            hash_[i] = [table[0][j] for j in duplicates(table[table[0].index(i)], 1)]
        print(hash_)

    MakeHash()

    ##########################################################################################################
    def route(v1, v2):
        if parents[v2] != "NONE":
            route(v1, parents[v2])
            print(v2)
        else:
            print(v2)

    queue += [v1]
    parents[v1] = "NONE"
    searched = []

    while queue:
        print(queue)
        city = queue.pop()

        if found:
            break
        if city not in searched:
            for i in hash_.get(city):
                if i not in parents:
                    parents[i] = city
                if i == v2:
                    print("")
                    print("")
                    print("")
                    print("done")
                    print("")
                    print("")
                    print("")
                    found = True
            else:
                queue += hash_[city]
                print(queue)
                searched.append(city)
        print(parents,searched)
        print("")
    if not found:
        print("Path doesn't Exist (used DFS)")
    else:
        print("\nThe paths using DFS are:  ")
        route(v1, v2)


if __name__ == '__main__':
    a = [['n/a', 'Atlanta', 'Austin', 'Chicago', 'Dallas', 'Denver', 'Houston', 'Boston', 'Venice', 'Belgium'],
         ['Atlanta', 0, 0, 1, 0, 0, 1, 1, 0, 0],
         ['Austin', 0, 0, 0, 1, 0, 1, 0, 0, 0],
         ['Chicago', 0, 0, 0, 1, 0, 0, 0, 0, 0],
         ['Dallas', 1, 0, 0, 0, 1, 0, 0, 0, 0],
         ['Denver', 1, 0, 1, 0, 0, 0, 0, 0, 0],
         ['Houston', 1, 0, 0, 0, 0, 0, 0, 0, 0],
         ['Boston', 1, 0, 0, 1, 0, 0, 0, 0, 0],
         ['Venice', 0, 0, 1, 0, 0, 0, 1, 0, 1],
         ['Belgium', 0, 0, 1, 0, 0, 0, 1, 0, 0]]

    # BFS(a, "Austin", "Chicago")
    BFS(a, "Belgium", "Houston")
    # BFS(a, "Venice", "Belgium")
    # BFS(a, "Venice", "Chicago")
