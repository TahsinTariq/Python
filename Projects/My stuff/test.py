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


from math import atan2, degrees
from collections import namedtuple
def angle(P1, P2, P3):
	return atan2(P3.y - P1.y, P3.x - P1.x) - atan2(P2.y - P1.y, P2.x - P1.x);

pt = namedtuple('pt', ['x', 'y'])

P1 = pt(0,0)
P2 = pt(1,1)
P3 = pt(0,1)

print(degrees(angle(P1, P2, P3)))


