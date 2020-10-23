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

import timeit

print(timeit.timeit('''

import random
from math import sqrt, atan2


def det(A):
    n = len(A)
    AM = A[:]

    for fd in range(n):
        if AM[fd][fd] == 0:
            AM[fd][fd] = 1.0e-18
        for i in range(fd+1, n):
            crScaler = AM[i][fd] / AM[fd][fd]
            for j in range(n):
                AM[i][j] = AM[i][j] - crScaler * AM[fd][j]

    product = 1.0
    for i in range(n):
        product *= AM[i][i]

    return product

def get_circle(a, b, c):
    vec = [a[0]**2 + a[1]**2, b[0]**2 + b[1]**2, c[0]**2 + c[1]**2]
    x_mat = [vec, [a[1], b[1], c[1]], [1]*3]
    y_mat = [vec, [a[0], b[0], c[0]], [1]*3]
    d_mat = [[a[0], b[0], c[0]], [a[1], b[1], c[1]], [1] * 3]
    d = 2 * det(d_mat)
    x = 1 / d * det(x_mat)
    y = -1 / d * det(y_mat)
    center = [x, y]
    r = norm([center[0]-a[0], center[1]-a[1]])
    return center, r

def get_circle_coords(center, r):
    circle = [[r, 180* phi/3.14159265] for phi in range(0, 180, 5)]
    circle = [pol2cart(p[0], p[1]) + (center[0], center[1]) for p in circle]
    return circle

def orientIfSure(px, py, rx, ry, qx, qy):
    l = (ry - py) * (qx - px)
    r = (rx - px) * (qy - py)
    if (abs(l - r) >= 3.3306690738754716*10**(-16) * abs(l + r)):
        return l - r
    else:
        return 0

def orient(rx, ry, qx, qy, px, py):
    return (orientIfSure(px, py, rx, ry, qx, qy) or orientIfSure(rx, ry, qx, qy, px, py) or orientIfSure(qx, qy, px, py, rx, ry)) < 0

def same_side(edge, p1, p2):
    x1, y1 = edge[0][0], edge[0][1]
    x2, y2 = edge[1][0], edge[1][1]
    ax, ay = p1[0], p1[1]
    bx, by = p2[0], p2[1]
    return orient(x1,y1, x2, y2, ax, ay) == orient(x1,y1, x2, y2, bx, by)

def get_distance(edge, center, r, candidate):
    p1, p2, p0 = edge[0], edge[1], center
    edge_len = norm([p2[0] - p1[0], p2[1] - p1[1]])
    sq = abs((p2[1]-p1[1])*p0[0] - (p2[0]-p1[0])*p0[1] + p2[0]*p1[1] - p2[1]*p1[0])
    dist = sq / edge_len
    if same_side(edge, center, candidate):
        return r + dist
    else:
        return r - dist

def point_in_arr(arr, point):
    for i in range(len(arr)):
        if arr[i][0] == point[0] and arr[i][1] == point[1]:
            return i
    return -1

def get_third_point(edge, triangles):
    for triangle in triangles:
        i1, i2 = point_in_arr(triangle, edge[0]), point_in_arr(triangle, edge[1])
        if not (i1 == -1 or i2 == -1):
            for i in range(len(triangle)):
                if not (i1 == i or i2 == i):
                    return triangle[i]
    return None

def get_mate(edge, points, triangles):
    best_point, best_dist = None, None
    third = get_third_point(edge, triangles)
    for point in points:
        if point_in_arr(edge, point) > -1:
            continue
        if third is not None and same_side(edge, point, third):
            continue
        center, r = get_circle(edge[0], edge[1], point)
        dist = get_distance(edge, center, r, point)
        if best_point is None or dist < best_dist:
            best_point, best_dist = point, dist
    return best_point

def edge_in_frontier(frontier, edge):
    if len(frontier) == 0:
        return None
    for frontier_edge in frontier:
        if frontier_edge == edge:
            return frontier_edge
        flipped = [frontier_edge[1], frontier_edge[0]]
        if flipped == edge:
            return frontier_edge
    return None

def remove_edge_from_frontier(frontier, edge):
    for i in range(len(frontier)):
        if frontier[i] == edge:
            frontier.remove(edge)
            break
    return frontier

def update_frontier(frontier, point, used_edge):
    edge1 = [used_edge[0], point]
    edge2 = [used_edge[1], point]
    used_edge = edge_in_frontier(frontier, used_edge)
    fr_edge1 = edge_in_frontier(frontier, edge1)
    fr_edge2 = edge_in_frontier(frontier, edge2)
    if used_edge is not None:
        frontier = remove_edge_from_frontier(frontier, used_edge)
    if fr_edge1 is not None:
        frontier = remove_edge_from_frontier(frontier, fr_edge1)
    else:
        frontier.append(edge1)
    if fr_edge2 is not None:
        frontier = remove_edge_from_frontier(frontier, fr_edge2)
    else:
        frontier.append(edge2)
    return frontier

def cart2pol(x, y):
    r = sqrt(x**2 + y**2)
    angle = atan2(y, x)
    return(r, angle)

def norm(vector):
    t = 0
    for i in vector:
        t = t+i*i
    return sqrt(t)

def hull_edge(points):
    p1 = points[0]
    for point in points:
        if point[1] < p1[1]:
            p1 = point
    p2 = points[0]
    min_angle = 3 * 3.14159265
    for point in points:
        if point == p1: continue
        vector = [point[0]-p1[0], point[1]-p1[1] ]
        angle = cart2pol(vector[0], vector[1])[1]
        if angle < min_angle:
            min_angle, p2 = angle, point
        elif angle == min_angle and norm(vector) > norm(p2 - p1):
            p2 = point
    return [p2, p1]

def delunay(points):
    triangles = []
    frontier = [hull_edge(points)]
    while frontier:
        edge, frontier = frontier[-1], frontier[:-1]
        mate = get_mate(edge, points, triangles)
        if mate is not None:
            frontier = update_frontier(frontier, mate, edge)
            triangle = [edge[0], edge[1], mate]
            triangles.append(triangle)
    return triangles



points = []
for i in range(1000):
    rnd = random.randint(0,640)
    rnd2 = random.randint(0,480)
    points.append((rnd, rnd2))

delunay(points)''', number=1))

# times = timeit.repeat(setup = setup,
#                           stmt = stmt,
#                           repeat = 1,
#                           number = 1)

# print(f'time: {min(times)}')

