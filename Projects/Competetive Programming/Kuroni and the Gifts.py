arr = []
t = int(input())
for i in range(t):
    arr.append([0, 0])

for j in range(t):
    n = input()
    arr[j][0] = []
    arr[j][1] = []
    a = input()
    for i in a.split():
        arr[j][0].append(int(i))
    b = input()
    for i in b.split():
        arr[j][1].append(int(i))
    arr[j][0] = sorted(arr[j][0])
    arr[j][1] = sorted(arr[j][1])
    print(*arr[j][0])
    print(*arr[j][1])
