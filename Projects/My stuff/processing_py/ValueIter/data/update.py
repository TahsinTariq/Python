from data.util import *
def update(temp):
    n_x = len(temp)
    n_y = len(temp[0])
    delta = 0
    for i in range(n_x):
        for j in range(n_y):
            if temp[i][j].isDigit:
                temp[i][j].pval = temp[i][j].val
    for i in range(n_x):
        for j in range(n_y):
            if temp[i][j].isDigit:
                cmax = 0
                # print("/n/n/n/n  iter: "+ str(iter))
                for a in actions:
                    c = 0
                    # print("/n"+ str(a))
                    for t in actions:
                        T = t
                        if not -1<i+T[0]<n_x or not -1<j+T[1]<n_y or temp[i+T[0]][j+T[1]].val == "b":
                            T = (0,0)
                        if not addTuple(a,t) == (0,0):
                            if addTuple(a,t) == addTuple(a,a) or addTuple(a,t) == a:
                                c += bellman(0.8, temp[i][j].pval, l, temp[i+T[0]][j+T[1]].pval)
                            else:
                                c += bellman(0.1, temp[i][j].pval, l, temp[i+T[0]][j+T[1]].pval)
                        # print(c)
                    if c > cmax:
                        cmax = c
                        temp[i][j].dir = (a[1],a[0])
                delta = max(delta, abs(cmax - temp[i][j].val))
                temp[i][j].val = cmax
    return delta, temp