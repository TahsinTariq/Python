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

a = {'S': [('d', 3), ('e', 9), ('p', 1)], 'a': [], 'b': [('a', 2)], 'c': [('a', 2)], 'd': [('b', 1), ('c', 8), ('e', 2)], 'e': [('r', 2), ('h', 8)], 'f': [('c', 3), ('G', 2)], 'h': [('p', 1), ('q', 1)], 'p': [('q', 15)], 'q': [], 'r': [('f', 2)], 'G': []}
for i , j in enumerate(a):
    print(i,j)
