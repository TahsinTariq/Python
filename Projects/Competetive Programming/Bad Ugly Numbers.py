t = int(input())
for _ in range(t):
    a = int(input())
    if a == 1:
        print("-1")
    else:
        print("2", end="")
        for i in range(a - 1):
            print("3", end="")
        print()
