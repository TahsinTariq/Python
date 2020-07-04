# print(50*'-')
# def duplicates(lst, item):
#     return [i for i, x in enumerate(lst) if x == item]
# n = int(input())
# a = list(map(int, input().split()))
# c = min(a.count(1), a.count(3), a.count(2))
# print(c)
# q = duplicates(a, 1)
# w = duplicates(a, 2)
# e = duplicates(a, 3)
# for i in range(c):
#     print(str(q[i]+1)+" "+str(w[i]+1)+" "+str(e[i]+1))
#
#
from decimal import Decimal
import math

n = list(map(int, input().split()))
a = sorted(n[1:], reverse= True)
d = math.floor(Decimal(n[0]) / Decimal(a[0]))
t = n[0]%a[0]
d += math.floor(Decimal(t)/ Decimal(a[1]))
t = t % a[1]
d += math.floor(Decimal(t)/ Decimal(a[2]))

print(d)






# a = list(map(int, input().split()))
# h = a.index(max(a))
# a.reverse()
# l = n - 1  - a.index(min(a))
# # print(h, l)
# if h < l:
#     print(n-l+h-1)
# else: print(n-2-l+h)
# print()
# a.sort()
# print(*a)

# s = input().split()
# for i in s:
#     if i != '':
#         print(i, end=" ")
