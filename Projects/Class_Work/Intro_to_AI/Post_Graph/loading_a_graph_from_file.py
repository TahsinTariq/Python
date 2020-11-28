arr = []
with open('grapp_for testing_BFSDFS.txt', "r") as f:
    for line in f:
        arr.append(line.split())

print(arr[0][0])
s = int(arr[0][0]) + 1
print(arr)
for j in range(s):
    for i in range(1, len(arr[j])):
        arr[j][i] = int(arr[j][i])
print(arr)
print(s)
a = []
a = [[i[0] for i in arr]]

temp = [0]
for i in arr[1:]:
    temp = [i[0]]
    print(temp)
    a.append(temp)
print(a)
a[0][0] = 'n/a'

for j in range(1, s):
    for i in range(1, s):
        a[j].append(0)
for line in arr[1:]:
    for i in line[1:]:
        a[arr.index(line)][i + 1] = 1


def show():
    print("\t\t", end="")
    for word in a[0]:
        print("", end='   ')
        print(word, end='')
    print("")
    for line in a[1:]:
        for word in line:
            print("\t", end='      ')
            print(word, end='')
        print("")


# for i in range(len(a)):
#     print([row[i] for row in a])
def enterEdge(v1, v2):
    a[v1 + 1][v2 + 1] = 1


# enterEdge(0, 2)
show()


def enterVertex(v_arr):
    a.append([v_arr[0]])
    a[0].append(v_arr[0])
    for j in a[1:-1]:
        j.append(0)
    for i in range(1, len((a[0]))):
        a[-1].append(0)
    for i in v_arr[1:]:
        enterEdge(a.index(a[-1]) - 1, i)

print("")
show()


import BFS_Using_Hash_grokking
import DFS_using_Hash
BFS_Using_Hash_grokking.BFS(a,"S","G")
DFS_using_Hash.BFS(a,"S","G")