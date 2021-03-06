def MinMax(node, depth, Is_Max):
    if depth == 0 or node in TerminalValue.keys():
        return TerminalValue[node]
    if Is_Max:
        value = -float('inf')
        for child in OwO[node]:
            # print(child)
            value = max(value, MinMax(child, depth, 0))
        return value
    else:
        value = float('inf')
        for child in OwO[node]:
            # print(child)
            value = min(value, MinMax(child, depth, 1))
        return value


if __name__ == '__main__':
    OwO = {}
    TerminalValue = {}
    # File contains Initial node.
    # If a node takes the max value, it is assigned 1; if min, 0. If it is a terminal node, it's assigned -1
    # Then it contains the child nodes number following child node names
    # Terminal nodes have 0 child nodes and one value

    with open('minmax_example', "r") as f:
        for line in f:
            arr = line.split()
            if int(arr[1]) >= 0:
                OwO[arr[0]] = [i for i in arr[3:]]
            else:
                TerminalValue[arr[0]] = int(arr[3])
        print(OwO)
        print(TerminalValue)
    print(MinMax('A', float('inf'), 1))
