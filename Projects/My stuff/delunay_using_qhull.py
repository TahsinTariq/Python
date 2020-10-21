from math import sqrt, atan2
from collections import namedtuple

def dist(a, b, c, d):
    """returns distance"""
    return sqrt((a -c)**2 +(b-d)**2)

class Point:

    def __init__(self, x, y):
        self.x, self.y = float(x), float(y)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __ne__(self, other):
        return not self == other

    def __gt__(self, other):
        if self.x > other.x:
            return True
        elif self.x == other.x:
            return self.y > other.y
        return False

    def __lt__(self, other):
        return not self > other

    def __ge__(self, other):
        if self.x > other.x:
            return True
        elif self.x == other.x:
            return self.y >= other.y
        return False

    def __le__(self, other):
        if self.x < other.x:
            return True
        elif self.x == other.x:
            return self.y <= other.y
        return False

    def __sub__(self, p):
        return Point(self.x - p.x, self.y-p.y)

    def __repr__(self):
        return f"Point : ({self.x}, {self.y})"

    def __hash__(self):
        return hash(self.x)

    # def inEdge(self, e):
    #     return self == Edge(t.a, t.b) or self == Edge(t.b, t.c) or self == Edge(t.c, t.a)

class Edge:

    def __init__(self, a, b):
        self.a, self.b = sorted((a, b))

    def __eq__(self, other):
        return self.a == other.a and self.b == other.b

    def __ne__(self, other):
        return not self == other

    def __repr__(self):
        return f"Edge : {(self.a, self.b)}"

    def __hash__(self):
        return hash(self.a+self.b)


def inCircle(self, p):
    """
        returns boolean whether the Point p is inside the circumCircle of the triangle
    """
    return dist(p.x, p.y, self.x, self.y)<=self.r

def circumCircle(self):
    """
        returns the center and the radius of the circumCircle of the triangle
    """
    circle = namedtuple('circle', ['x', 'y', 'r'])
    a,b,c = self.a, self.b, self.c
    d = 2 * (a.x * (b.y - c.y) + b.x * (c.y - a.y) + c.x * (a.y - b.y))
    ua = ((a.x * a.x + a.y * a.y) * (b.y - c.y) + (b.x * b.x + b.y * b.y) * (c.y - a.y) + (c.x * c.x + c.y * c.y) * (a.y - b.y)) / d
    ub = ((a.x * a.x + a.y * a.y) * (c.x - b.x) + (b.x * b.x + b.y * b.y) * (a.x - c.x) + (c.x * c.x + c.y * c.y) * (b.x - a.x)) / d

    A = self.area()
    x = ua
    y = ub
    den = 4*A
    num = ( (((b.x-a.x)**2) + ((b.y-a.y)**2)) * (((c.x-b.x)**2)+((c.y-b.y)**2)) * (((a.x-c.x)**2)+((a.y-c.y)**2)) )**(0.5)
    R = abs(num/den)
    self.x, self.y ,self.r = x,y,R
    cir = circle(x,y,R)
    return cir

def sharesVertex(self, t):
    for i in (self.a, self.b, self.c):
        for j in (t.a, t.b, t.c):
            if i==j:
                return True
    return False

def _construct_points(list_of_tuples):
    points = []
    if list_of_tuples:
        for p in list_of_tuples:
            try:
                points.append(Point(p[0], p[1]))
            except (IndexError, TypeError):
                print(
                    f"Ignoring deformed point {p}. All points"
                    " must have at least 2 coordinates."
                )
    return points


def _validate_input(points):
    if not points:
        raise ValueError(f"Expecting a list of points but got {points}")

    if isinstance(points, set):
        points = list(points)

    try:
        if hasattr(points, "__iter__") and not isinstance(points[0], Point):
            if isinstance(points[0], (list, tuple)):
                points = _construct_points(points)
            else:
                raise ValueError(
                    "Expecting an iterable of type Point, list or tuple. "
                    f"Found objects of type {type(points[0])} instead"
                )
        elif not hasattr(points, "__iter__"):
            raise ValueError(
                f"Expecting an iterable object but got an non-iterable type {points}"
            )
    except TypeError:
        print("Expecting an iterable of type Point, list or tuple.")
        raise

    return points


def _det(a, b, c):
    det = (a.x * b.y + b.x * c.y + c.x * a.y) - (a.y * b.x + b.y * c.x + c.y * a.x)
    return det


def convex_hull_recursive(points):

    points = sorted(_validate_input(points))
    n = len(points)

    left_most_point = points[0]
    right_most_point = points[n - 1]

    convex_set = {left_most_point, right_most_point}
    upper_hull = []
    lower_hull = []

    for i in range(1, n - 1):
        det = _det(left_most_point, right_most_point, points[i])

        if det > 0:
            upper_hull.append(points[i])
        elif det < 0:
            lower_hull.append(points[i])

    _construct_hull(upper_hull, left_most_point, right_most_point, convex_set)
    _construct_hull(lower_hull, right_most_point, left_most_point, convex_set)

    return sorted(convex_set)


def _construct_hull(points, left, right, convex_set):
    if points:
        extreme_point = None
        extreme_point_distance = float("-inf")
        candidate_points = []

        for p in points:
            det = _det(left, right, p)

            if det > 0:
                candidate_points.append(p)

                if det > extreme_point_distance:
                    extreme_point_distance = det
                    extreme_point = p

        if extreme_point:
            _construct_hull(candidate_points, left, extreme_point, convex_set)
            convex_set.add(extreme_point)
            _construct_hull(candidate_points, extreme_point, right, convex_set)

def cart2pol(x, y):
    """Cartesian coordinates to polar"""
    r = sqrt(x**2 + y**2)
    φ = atan2(y, x)
    return (r, φ)

def cmp_angle(φ_1, φ_2):
    """Angle comparison"""
    return φ_2 - φ_1

def same_side(edge, p1, p2):
    """Check if points p1 and p2 are on the same side of edge"""
    edge_vec = edge.a - edge.b
    p1_vec, p2_vec = p1 - edge.a, p2 - edge.a
    edge_angle = cart2pol(edge_vec.x, edge_vec.y)[1]
    p1_angle, p2_angle = cart2pol(p1_vec.x, p1_vec.y)[1], cart2pol(p2_vec.x, p2_vec.y)[1]
    p1_delta, p2_delta = cmp_angle(edge_angle, p1_angle), cmp_angle(edge_angle, p2_angle)
    return p1_delta * p2_delta > 0

def get_distance(edge, center, r, candidate):
    """Distance from an edge to the other end of the circle.
     candidate indicates which side to read from"""
    p1, p2, p0 = edge.a, edge.b, center
    # edge_len = dist(p1.x, p1.y, p2.x, p2.y)
    edge_len = sqrt((p1.x -p2.x)**2 +(p1.y-p2.y)**2)
    sq = abs((p2.y-p1.y)*p0[0] - (p2.x-p1.x)*p0[1] + p2.x*p1.y - p2.y*p1.x)
    dist = sq / edge_len
    if same_side(edge, Point(center[0], center[0]), candidate):
        return r + dist
    else:
        return r - dist

def get_third_point(edge, triangles):
    """Get conjugate point for an edge from known triangles"""
    for triangle in triangles:
        # i1, i2 = point_in_arr(triangle, edge[0]), point_in_arr(triangle, edge[1])
        if edge.inTriangle(triangle):
            if edge == Edge(t.a, t.b):
                return t.c
            elif edge == Edge(t.b, t.c):
                return t.a
            else: return t.a
        # if not (i1 == -1 or i2 == -1):
        #     for i in range(len(triangle)):
        #         if not (i1 == i or i2 == i):
        #             return triangle[i]
    return None

def get_mate(edge, points, triangles):
    """Get a new mating point"""
    best_point, best_dist = None, None
    points = list(set([e.a for e in points] + [e.b for e in points]))
    print(f'points: {points}')
    third = get_third_point(edge, triangles)
    for point in points:
        # if point_in_arr(edge, point) > -1:
        if edge.a == point or edge.b == point:
            continue
        if third is not None and same_side(edge, point, third):
            continue
        # center, r = get_circle(*edge, point)
        x, y , r = Triangle(edge.a, edge.b, point).circumCircle()
        center = (x,y)
        dist = get_distance(edge, center, r, point)
        if best_point is None or dist < best_dist:
            best_point, best_dist = point, dist
    print(f"Best Point : {best_point}")
    return best_point

def delunay(points):
    triangles = []
    hull_edges = convex_hull_recursive(points)
    # print(hull_edges)
    frontier = [Edge(hull_edges[0], hull_edges[1])]
    # print(frontier)
    # print(frontier[-1], frontier[:-1])
    while frontier:
        edge, frontier = frontier[-1], frontier[:-1]
        mate = get_mate(edge, frontier, triangles)
        if mate is not None:
            frontier = update_frontier(frontier, mate, edge)
            # triangle = np.array([*edge, mate])
            triangles.append(triangle)









if __name__ == "__main__":
    # points = [(0, 3),(2, 2),(1, 1),(2, 1),(3, 0),(0, 0),(3, 3),(2, -1),(2, -4),(1, -3)]
    points = [(1,2), (3,8), (6, 10), (7,5), (8,9)]

    # results_recursive = convex_hull_recursive(points)

    # print(results_recursive)

    # delunay(points)



    p = _validate_input(points)
    e1 = Edge(p[0], p[1])
    e2 = Edge(p[2], p[4])
    e3 = Edge(p[1], p[2])
    e4 = Edge(p[1], p[3])
    t = Triangle(p[0], p[1], p[2])
    val = e4.inTriangle(t)
    # print(val)

    hull_edges = convex_hull_recursive(points)
    # print(hull_edges)
    frontier = [Edge(hull_edges[0], hull_edges[-2])]
    get_mate(e2, [e2,e3,e4], [Triangle(p[0],p[1],p[3])])
    print(frontier)
