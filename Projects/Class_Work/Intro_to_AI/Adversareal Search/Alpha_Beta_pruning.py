def AlphaBeta(node, depth, Alpha, Beta, Is_Max):
    if depth == 0 or node in TerminalValue.keys():
        return TerminalValue[node]
    if Is_Max:
        value = -float('inf')
        for child in OwO[node]:
            print(child)
            value = max(value, AlphaBeta(child, depth - 1, Alpha, Beta, 0))
            Alpha = max(Alpha, value)
            if Alpha >= Beta:
                break
        return value
    else:
        value = float('inf')
        for child in OwO[node]:
            print(child)
            value = min(value, AlphaBeta(child, depth - 1, Alpha, Beta, 1))
            Beta = min(Beta, value)
            if Alpha >= Beta:
                break
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
        # print(OwO)
        # print(TerminalValue)
    print("Searched Through: ")
    c = AlphaBeta('A', float('inf'), -float('inf'), float('inf'), 1)
    print("\n"+ "Max Utility: " + str(c))
