a = int(input())
a = list(map(int, input().split()))
x = max(a[0], 0 )
print(a[0], end=" ")
for i in range(1, len(a)):
    print(x+a[i], end=" ")
    x = max(x,x+a[i])
