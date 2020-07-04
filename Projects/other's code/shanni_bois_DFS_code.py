file = open('grapp_shanni_boi.txt', 'r')
# print(file.read())
list = []
node_num = int(file.readline())  # node_num = 7
for line in file:
    list.append(line.split())
# print(list)
row_num = node_num + 1  # row_num = 8
# print(row_num)
for i in range(row_num - 1):
    for j in range(len(list[i])):
        list[i][j] = int(list[i][j])
print("\nInput:")
for i in range(row_num - 1):
    print(list[i])

edge_table = [0] * row_num
for i in range(row_num):
    edge_table[i] = [0] * row_num

for k in range(1, row_num):
    edge_table[0][k] = k - 1
for k in range(1, row_num):
    edge_table[k][0] = k - 1

for i in range(1, len(list) + 1):
    for j in range(1, len(list[i - 1])):
        s = list[i - 1][j]
        # print(s)
        edge_table[i][s + 1] = 1

print("\nEdge Table:")
for i in range(row_num):
    print(edge_table[i])

file.close()


def addEdge(edge1, edge2):
    edge_table[edge1 + 1][edge2 + 1] = 1


def addVertex(edges):
    p = edge_table[-1][0] + 1
    edge_table.append([p])
    edge_table[0].append(p)
    for j in edge_table[1:-1]:
        j.append(int(0))
    for i in range(1, len((edge_table[0]))):
        edge_table[-1].append(0)
    for i in edges:
        addEdge(p, i)


print('\nVertex Added:')
addVertex([2, 3])


def show():
    for i in range(edge_table[-1][0] + 2):
        print(edge_table[i])


show()


def dfs(source, goal):
    stack = []
    mark = [0] * (len(edge_table[0]) - 1)
    pred = [-1] * (len(edge_table[0]) - 1)
    found = False
    stack.append(source)

    while not found:
        top = stack.pop()
        if top == goal:
            found = True
        count = 0
        for i in edge_table[top + 1]:
            if i == 1:
                stack.append(count)
                pred[count] = top
                count += 1
            elif i == 0:
                count += 1
            else:
                pass
        mark[top] = 1
        # for i in stack:
        #     pred[i]=top

        print("\npred\n", pred)
        print("\nmark\n", mark)
        print("\nStack: ")
        print(stack)


dfs(2, 5)
