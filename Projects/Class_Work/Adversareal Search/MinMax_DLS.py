def MinMax_DLS(node, depth, Is_Max):
    if depth == 0:
        return EvalFunction[node]
    if node in TerminalValue.keys():
        return TerminalValue[node]
    if Is_Max:
        value = -float('inf')
        for child in OwO[node]:
            print(child)
            value = max(value, MinMax_DLS(child, depth-1, 0))
        return value
    else:
        value = float('inf')
        for child in OwO[node]:
            print(child)
            value = min(value, MinMax_DLS(child, depth-1, 1))
        return value


if __name__ == '__main__':
    OwO = {}
    MinOrMax = {}
    TerminalValue = {}
    EvalFunction = {}

    # File contains Initial node.
    # If a node takes the max value, it is assigned 1; if min, 0. If it is a terminal node, it's assigned -1
    # Then it contains the child nodes number following child node names
    # Terminal nodes have 0 child nodes and one value
    # The last value for non terminal nodes are the Evaluation function estimates

    with open('wiki_minmax_example_DLS', "r") as f:
        for line in f:
            arr = line.split()
            if int(arr[1]) >= 0:
                OwO[arr[0]] = [i for i in arr[3:-1]]
                EvalFunction[arr[0]] = int(arr[-1])
            else:
                TerminalValue[arr[0]] = int(arr[3])
        # print(OwO)
        # print(TerminalValue)
        # print(EvalFunction)
    print("Searched Through: ")
    # c = MinMax_DLS('a', float('inf'), 1)
    c = MinMax_DLS('a', 3, 1)
    print("\n"+ "Max Utility: " + str(c))