from numpy import *

arr = []
with open('grapp.txt', "r") as f:
    for line in f:
        arr.append(line.split())
    s = int(line[0][0]) + 2
    for line in arr:
        for j in range(s):
            for i in range(1,len(arr[j])):
                arr[j][i]= int(arr[j][i])
    print(s)
    print("")
    a = zeros((s, s))
    for i in range(1,s):
        a[0][i] = i-1
        a[i][0] = i - 1
    a[0][0] = 0
    print(arr)
    print("")

    for i in range(1, s):
        for j in range(len(arr[i])):
            if j != 0:
                k = int(arr[i][j])
                a[i, k + 1] = 1
    print(a)
    print("")


    def edge(v1, v2):
        a[v1 + 1][v2 + 1] = 1


    edge(5, 6)
    print(a)
    print("")

    arr.append(['atlanta', 2, 3])
    ns = int(arr[0][0]) + 2
    print(ns)
    print("")
    a = zeros((ns, ns))
    for i in range(ns):
        a[0][i] = i - 1
        a[i][0] = i - 1
    a[0][0] = 0
    print(arr)
    print("")

    for i in range(1, ns):
        for j in range(len(arr[i])):
            if j != 0:
                k = int(arr[i][j])
                a[i, k + 1] = 1
    print(a)
