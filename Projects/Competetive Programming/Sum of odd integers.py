t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    if n%2 != k%2 or (k > n**.5 ):
        print("NO")
    else: print("YES")