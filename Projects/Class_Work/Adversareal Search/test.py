def MinMax(node, depth, Is_Max):
    if depth == 0 or node in TerminalValue.keys():
        return TerminalValue[node]
    if Is_Max:
        value = -float('inf')
        pval = -float('inf')
        for child in OwO[node]:
            print(child)
            value = max(value, MinMax(child, depth, 0))
            if pval < value:
                pval = value
                path[child] = node
        return value
    else:
        value = float('inf')
        pval = float('inf')
        for child in OwO[node]:
            print(child)
            value = min(value, MinMax(child, depth, 1))
            if pval > value:
                pval = value
                path[child] = node
        return value


def find(p):
    print(p)
    if p == "A":
        return None
    else:
        find(path[p])


if __name__ == '__main__':
    OwO = {}
    MinOrMax = {}
    TerminalValue = {}
    path = {}
    # File contains Initial node.
    # If a node takes the max value, it is assigned 1; if min, 0. If it is a terminal node, it's assigned -1
    # Then it contains the child nodes number following child node names
    # Terminal nodes have 0 child nodes and one value

    with open('minmax_cw', "r") as f:
        for line in f:
            arr = line.split()
            if int(arr[1]) >= 0:
                OwO[arr[0]] = [i for i in arr[3:]]
                MinOrMax[arr[0]] = arr[1]

            else:
                TerminalValue[arr[0]] = int(arr[3])
        print(OwO)
        print("\n")
        print(MinOrMax)
        print("\n")
        for i in OwO.keys():
            if int(MinOrMax[i]) == 1:
                print("Node: " + i + "\nType: MAX" + "\nChild DIE!  :")
            else:
                print("Node: " + i + "\nType: MIN" + "\nChild:")
            for j in OwO[i]:
                print(j)
            print("Number of Chlidren: " + str(len(OwO[i])))
            print("\n")
        for i in TerminalValue.keys():
            print("Node: " + i + "\nCondition: Terminal" + "\nValue: " + str(TerminalValue[i]) + "\n")

    ans = MinMax('A', float('inf'), 1)
    for key in TerminalValue.keys():
        if TerminalValue[key] == ans:
            find(key)
            break

    print('\nvalue :  ' + str(ans))

    print(path)
