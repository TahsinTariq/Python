# T = int(input())
# for _ in range(T):
#     n = int(input())
#     A = sorted(list(map(int, input().split())))
#     B = sorted(list(map(int, input().split())))
#
#     print(*A)
#     print(*B)

# from Class_Work.Graph import Search
#
# pq = Search.PriorityQueue()
# pq.push('a', 5)
# pq.push('b', 2)
# pq.push('c', 7)
# pq.push('d', 1)
# pq.push('e', 10)
# pq.push('f', 6)
# pq.pop()
# pq.pop()
# pq.pop()
# pq.pop()
# pq.pop()
# pq.pop()
# import heapq
# from heapq import *

# a = [5,2,7,1,10]
# heappush(a, 6)
# a = []
# heappush(a, 5)
# heappush(a, 2)
# heappush(a, 7)
# heappush(a, 1)
# heappush(a, 10)
# heappush(a, 6)
#
# while a:
#     print(heappop(a))
#
#
# b = [1,2,3,4]
# print(b)
# print(b+1)

# x = (lambda x : x % 2 and 'odd' or 'even')
# print(x(2))

# a = {'S': [('d', 3), ('e', 9), ('p', 1)], 'a': [], 'b': [('a', 2)], 'c': [('a', 2)], 'd': [('b', 1), ('c', 8), ('e', 2)], 'e': [('r', 2), ('h', 8)], 'f': [('c', 3), ('G', 2)], 'h': [('p', 1), ('q', 1)], 'p': [('q', 15)], 'q': [], 'r': [('f', 2)], 'G': []}
# for i , j in enumerate(a):
#     print(i,j)

# def addF(a: int, b:int =3) -> int:
#     if not (isinstance(a, int) and isinstance(b, int)):
#         raise ValueError("Both must be integers")
#     return a+b
# print(addF(2))
# for i in range(2*5):
#     print(i/2)

# print(abs(-1.5))

# l = {1,2,3,4}
# print(type(l))



# class test(object):
# 	"""docstring for test"""
# 	def __init__(self, arg):
# 		self.arg = arg

# 	def __add__(self, arg):
# 		return self.arg - arg.arg

# a =test(5)
# b = test(6)
# c =a+b
# print(c)
# print(dir(a))


# from math import atan2, degrees
# from collections import namedtuple
# def angle(a, b, c):
#     return atan2( c.y - b.y,  c.x - b.x) - atan2(a.y - b.y, a.x - b.x);

# pt = namedtuple('pt', ['x', 'y'])

# a = pt(1,1)
# b = pt(0,0)
# c = pt(0,1)

# print(degrees(angle(a,b,c)))

# p = [(0, 3), (2, 2), (1, 1), (2, 1), (3, 0), (0, 0), (3, 3), (2, -1), (2, -4), (1, -3)]

# print(p.sort())



# from matplotlib import pyplot as plt
# points = [
#         (0, 3),
#         (2, 2),
#         (1, 1),
#         (2, 1),
#         (3, 0),
#         (0, 0),
#         (3, 3),
#         (2, -1),
#         (2, -4),
#         (1, -3),
#     ]
# # P = [(-12.5, -7.5), (1.5, 13.5), (15.5, -7.5),(-12.5, -7.5)]
# P = [(1.0, 1.0), (2.0, 1.0), (15.5, -7.5),(1.0, 1.0)]
# '''
# Q = set(
#     [((0.0, 0.0), (0.0, 3.0), (1.0, 1.0)), ((0.0, 3.0), (1.0, -3.0), (1.0, 1.0)), ((0.0, 0.0), (1.0, -3.0), (2.0, -1.0)), ((1.0, -3.0), (1.0, 1.0), (2.0, -1.0)), ((0.0, 0.0), (1.0, 1.0), (2.0, -1.0)), ((1.0, 1.0), (2.0, -4.0), (2.0, -1.0)), ((1.0, -3.0), (2.0, -4.0), (2.0, -1.0)), ((0.0, 3.0), (2.0, -1.0), (2.0, 1.0)), ((0.0, 3.0), (1.0, 1.0), (2.0, 2.0)), ((1.0, 1.0), (2.0, 1.0), (2.0, 2.0)), ((0.0, 3.0), (2.0, 1.0), (2.0, 2.0)), ((0.0, 0.0), (2.0, -1.0), (3.0, 0.0)), ((1.0, -3.0), (2.0, -1.0), (3.0, 0.0)), ((2.0, -4.0), (2.0, 1.0), (3.0, 0.0)), ((1.0, 1.0), (2.0, -4.0), (3.0, 0.0)), ((1.0, 1.0), (2.0, 1.0), (3.0, 0.0)), ((2.0, -1.0), (2.0, 1.0), (3.0, 0.0)), ((2.0, -1.0), (2.0, 2.0), (3.0, 0.0)), ((0.0, 0.0), (2.0, 2.0), (3.0, 0.0)),  ((1.0, 1.0), (2.0, 1.0), (3.0, 3.0)), ((2.0, -4.0), (2.0, 1.0), (3.0, 3.0)), ((0.0, 3.0), (2.0, 2.0), (3.0, 3.0)), ((2.0, 1.0), (2.0, 2.0), (3.0, 3.0)), ((2.0, 1.0), (3.0, 0.0), (3.0, 3.0)), ((2.0, 2.0), (3.0, 0.0), (3.0, 3.0)), ]
#     )
# '''
# Q = set(
#     [((0.0, 0.0), (0.0, 2.0), (2.0, 0.0)), ((0.0, 0.0), (1.0, 3.0), (2.0, 0.0)), ((0.0, 0.0), (0.0, 2.0), (3.0, 1.0)), ((0.0, 2.0), (1.0, 3.0), (3.0, 1.0)), ((1.0, 3.0), (2.0, 0.0), (3.0, 1.0)), ((0.0, 2.0), (2.0, 0.0), (3.0, 1.0))]
#     )
# print(Q)
# print(set(Q))
# # plt.plot([i[0] for i in points], [i[1] for i in points], label='points')
# # plt.plot([i[0] for i in P], [i[1] for i in P], label='P')

# for q in Q:
#     x = [i[0] for i in q]
#     x.append(q[0][0])
#     y = [i[1] for i in q]
#     y.append(q[0][1])
#     plt.plot(x,y)


# plt.grid(True)
# plt.tight_layout()
# plt.show()
# print(points[3:4])
# print([i[0] for i in points]+[i[1] for i in points])

# from math import sqrt, atan2, degrees, dist
# print(degrees(atan2(0, -1)))





# def function(edge, p1, p2):
#     x1, y1 = edge[0]
#     x2, y2 = edge[1]
#     ax, ay = p1[0], p1[1]
#     bx, by = p2[0], p2[1]
#     m = y2 - y1/(x2-x1)
#     c = y1 - x1*m
#     eq1 = ax - ay/m + c/m
#     eq2 = bx - by/m + c/m
#     return eq1*eq2 >0

# import tensorflow as tf
# print(tf.version.VERSION)

# import datetime
# print(datetime.datetime.now().strftime("%H:%M:%S"))
print("editing test file for git?")
