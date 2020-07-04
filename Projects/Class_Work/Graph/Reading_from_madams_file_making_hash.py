import Dijkstra

arr = []
OwO = {}
with open('grapp_madam_test.txt', "r") as f:
    for line in f:
        arr = line.split()
        if arr[0].isdigit():
            continue
        OwO[arr[0]] = {}
        for i in range(1, len(arr[1:]), 2):
            OwO[arr[0]][arr[i]] = int(arr[i + 1])
###########     APSP     #########
for i in OwO:
    for j in OwO:
        print("path from ", i, 'to', j)
        Dijkstra.DJ(OwO, i, j)
