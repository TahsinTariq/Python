arr = []
OwO = {}
h = {}
with open('Romanian_roadmap', "r") as f:
    for line in f:
        arr = line.split()
        if arr[0].isdigit():
            continue
        OwO[arr[0]] = {}
        h [arr[0]] = int(arr[1])
        for i in range(2, len(arr[1:]), 2):
            OwO[arr[0]][arr[i]] = int(arr[i + 1])

print(OwO)
print("\n",h)
h = {k: v for k, v in sorted(h.items(), key=lambda item: item[1], reverse = True )}
print(h)
# h.popitem()
# print(h)
# h.popitem()
# print(h)

