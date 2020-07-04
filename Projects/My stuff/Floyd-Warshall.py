def FW(arr):
    l = len(arr[0]) - 1
    dist = [[0 for _ in range(l)] for _ in range(l)]
    for i in range(len(arr[1:])):
        for j in range(len(arr[1:])):
            if i != j:
                if arr[i + 1][j + 1] > 0:
                    dist[i][j] = arr[i + 1][j + 1]
                else:
                    dist[i][j] = float("inf")
    for k in range(l):
        for i in range(l):
            for j in range(l):
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
    for line in range(l):
        for city in range(l):
            print("Shortest distance from ", arr[0][line + 1], "to ", arr[0][city + 1], " is : ", dist[line][city])


if __name__ == '__main__':
    arr = [['n/a', 'Atlanta', 'Austin', 'Chicago', 'Dallas', 'Denver', 'Houston', 'Boston'],
           ['Atlanta', 0, 0, 0, 0, 0, 800, 600],
           ['Austin', 0, 0, 0, 200, 0, 160, 0],
           ['Chicago', 0, 0, 0, 0, 1000, 0, 0],
           ['Dallas', 0, 200, 0, 0, 780, 0, 0],
           ['Denver', 1400, 0, 0, 0, 0, 0, 0],
           ['Houston', 800, 0, 0, 0, 0, 0, 0],
           ['Boston', 600, 0, 0, 1300, 0, 0, 0]]
    FW(arr)
