from matplotlib import pyplot as plt

S = [
        (0, 3),
        (2, 2),
        (1, 1),
        (2, 1),
        (3, 0),
        (0, 0),
        (3, 3),
        (2, -1),
        (2, -4),
        (1, -3),
    ]


def quickHull(s):
    convexHull = []
    leftMost = min(s, key=lambda x:x[0])
    rightMost = max(s, key=lambda x:x[0])
    convexHull.append(leftMost)
    convexHull.append(rightMost)
    s.remove(rightMost)
    s.remove(leftMost)
    # print(s)
    s1 = []
    s2 = []
    for pt in s:
        n = ((rightMost[0] - leftMost[0]) * (pt[1] - leftMost[1]) -(rightMost[1] - leftMost[1]) * (pt[0] - leftMost[0]))
        if n > 1:
            s1.append(pt)
        if n<1:
            s2.append(pt)
    # print(s1)
    # print(s2)
    findHull(s1, leftMost, rightMost)
    findHull(s1, rightMost, leftMost)
    print(convexHull)

def findHull(sk, p, q):
    if not sk:
        return 0



if __name__ == '__main__':
    # print(sorted(S, reverse = True))
    quickHull(S)

    # S.sort(key = lambda x:x[0])
    # plt.plot([i for i, j in S], [j for i, j in S], label='Python')
    # plt.tight_layout()
    # plt.grid(True)
    # plt.show()