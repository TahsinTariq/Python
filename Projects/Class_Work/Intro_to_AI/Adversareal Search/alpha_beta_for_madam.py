def AlphaBeta(node, depth, Alpha, Beta, Is_Max):
    if depth == 0 or node in TerminalValue.keys():
        return TerminalValue[node]
    if Is_Max:
        value = -float('inf')
        pval = -float('inf')
        for child in OwO[node]:
            print(child + " Alpha :" + str(Alpha))
            value = max(value, AlphaBeta(child, depth - 1, Alpha, Beta, 0))
            if pval < value:
                pval = value
                parents[child] = node
            Alpha = max(Alpha, value)
            if Alpha >= Beta:
                break
        return value
    else:
        value = float('inf')
        pval = float('inf')
        for child in OwO[node]:
            print(child + " Beta : " + str(Beta))
            value = min(value, AlphaBeta(child, depth - 1, Alpha, Beta, 1))
            if pval > value:
                pval = value
                parents[child] = node
            Beta = min(Beta, value)
            if Alpha >= Beta:
                break
        return value


def find(p):
    path.append(p)
    if p == "a":
        return None
    else:
        find(parents[p])

if __name__ == '__main__':
    OwO = {}
    path = []
    parents = {}
    TerminalValue = {}

    # File contains Initial node.
    # If a node takes the max value, it is assigned 1; if min, 0. If it is a terminal node, it's assigned -1
    # Then it contains the child nodes number following child node names
    # Terminal nodes have 0 child nodes and one value

    with open('minmax_Madam', "r") as f:
        for line in f:
            arr = line.split()
            if int(arr[1]) >= 0:
                OwO[arr[0]] = [i for i in arr[3:]]
            else:
                TerminalValue[arr[0]] = int(arr[3])
        # print(OwO)
        # print(TerminalValue)
    print("Searched Through: ")
    c = AlphaBeta('a', float('inf'), -float('inf'), float('inf'), 1)
    print("\n"+ "Max Utility: " + str(c))

    for key in TerminalValue.keys():
        if TerminalValue[key] == c:
            find(key)
            break

    path.reverse()

    print("The path is :")
    print(path)
