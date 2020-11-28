def find(table, old, v1, v2):
    if v1 != v2:
        find(table, old, v1, table[0][old.index(v2) + 1])
        print(v2)
    else:
        print(v2)


def DFS(table, v1, v2):
    stack = []
    mark = [0] * (len(table[0]) - 1)
    old = [0] * (len(table[0]) - 1)
    granddad = []
    found = False
    pos1 = table[0].index(v1)
    pos2 = table[0].index(v2)
    stack.append(v1)
    print(stack)
    # stack.append(v2)
    run = 0
    place = pos1
    index = 0
    while not found:
        try:
            place = table[0].index(stc) - 1
        except:
            pass
        stc = stack.pop()
        print("removing : ", stc)
        if stc == v2:
            found = True
        s_pos = table[0].index(stc)
        if mark[s_pos - 1] != 1:
            mark[s_pos - 1] = 1
        else:
            continue
        if s_pos != pos1:
            old[place] = stc
        # index = 0
        for i in table[s_pos][1:]:
            if i > 0:
                p = table[0][table[s_pos][index:].index(i) + index]
                index = table[s_pos].index(i) + 1
                if mark[table[0].index(p) - 1] != 1:
                    stack.append(p)
                    print('inserting : ', p)
                    # old[table[s_pos][index:].index(i) + index] = 1
                    print(stack, end="  ")
                    print(mark, end="  ")
                    print(old, end="")
                    print(index)
                else:
                    print("not inserting : ", p)
        if found == True:
            find(table, old, v1, v2)
            break
        if not stack:
            print("No path found")
            break


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

    DFS(a, "Belgium", "Atlanta")
