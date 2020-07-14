import numpy as np

class Object:
    def __init__(self, name, value, weight):
        self.name = name
        self.weight = weight
        self.value = value

def addToList(grid, newObj):
    l = len(grid[0])
    grid.append([])
    for i in range(l):
        if i ==0:
            grid[-1].append(Object("Add to KnapSack:", 0,0))
        elif newObj.weight> i:
            grid[-1].append(grid[-2][i])
        else:
            otherObject = grid[-2][i - newObj.weight]
            if otherObject.value + newObj.value > grid[-2][i].value:
                grid[-1].append(Object(f"{otherObject.name}\n{newObj.name}",
                                            otherObject.value + newObj.value,
                                            otherObject.weight + newObj.weight))
            else: grid[-1].append(grid[-2][i])
    return grid

def knapSack(objList, cap):
    n = len(objList)
    grid = []
    # grid = np.zeros((n+1, cap+1))
    for i in range(n+1):
        grid.append([])
        for j in range(cap+1):
            grid[i].append([])
    for i in range(n+1):
        for j in range(cap+1):
            if i == 0 or j == 0:
                grid[i][j] = Object("Add to KnapSack:", 0,0)
            elif objList[i-1].weight > j:
                grid[i][j] = grid[i-1][j]
                # grid[i][j] = Object(grid[i-1][j].name,grid[i-1][j].value, grid[i-1][j].weight)
            else:
                # grid[i][j] = max(grid[i-1][j - objList[i-1].weight]+objList[i-1].value, grid[i-1][j])
                otherObject = grid[i - 1][j - objList[i - 1].weight]
                if otherObject.value + objList[i - 1].value> grid[i - 1][j].value:
                    grid[i][j] = Object(f"{otherObject.name}\n{objList[i - 1].name}",
                                        otherObject.value + objList[i - 1].value,
                                        otherObject.weight + objList[i - 1].weight)
                # else: grid[i][j] = Object(f"{grid[i - 1][j].name}", grid[i - 1][j].value ,grid[i - 1][j].weight)
                else: grid[i][j] = grid[i - 1][j]
    return grid

if __name__ == '__main__':
    obj = [("Guitar", 1500, 1), ("Stereo", 3000, 4), ("Laptop", 2000, 3)]
    objList = []
    for i in obj:
        objList.append(Object(i[0], i[1], i[2]))
    capacity = 4
    grid = knapSack(objList, capacity)
    print(grid[-1][-1].value)
    print(grid[-1][-1].name)
    phone = Object("IPhone", 2000, 1)
    grid = addToList(grid, phone)
    print(grid[-1][-1].value)
    print(grid[-1][-1].name)