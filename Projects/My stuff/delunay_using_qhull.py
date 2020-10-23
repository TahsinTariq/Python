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


def det(A):
    """
    Create an upper triangle matrix using row operations.
        Then product of diagonal elements is the determinant
        :param A: the matrix to find the determinant for
        :return: the determinant of the matrix
    """
    # Section 1: Establish n parameter and copy A
    n = len(A)
    AM = A[:]

    # Section 2: Row manipulate A into an upper triangle matrix
    for fd in range(n):  # fd stands for focus diagonal
        if AM[fd][fd] == 0:
            AM[fd][fd] = 1.0e-18  # Cheating by adding zero + ~zero
        for i in range(fd+1, n):  # skip row with fd in it.
            crScaler = AM[i][fd] / AM[fd][fd]  # cr stands for "current row".
            for j in range(n):  # cr - crScaler * fdRow, one element at a time.
                AM[i][j] = AM[i][j] - crScaler * AM[fd][j]

    # Section 3: Once AM is in upper triangle form ...
    product = 1.0
    for i in range(n):
        product *= AM[i][i]  # ... product of diagonals is determinant

    return product

def get_circle(a, b, c):
    """Get the coordinates of the center and radius of a circle through three points"""
    vec = [a[0]**2 + a[1]**2, b[0]**2 + b[1]**2, c[0]**2 + c[1]**2]
    x_mat = [vec, [a[1], b[1], c[1]], [1]*3]
    y_mat = [vec, [a[0], b[0], c[0]], [1]*3]
    d_mat = [[a[0], b[0], c[0]], [a[1], b[1], c[1]], [1] * 3]
    d = 2 * det(d_mat)
    x = 1 / d * det(x_mat)
    y = -1 / d * det(y_mat)
    center = [x, y]
#     r = norm(center - a)
    r = norm([center[0]-a[0], center[1]-a[1]])
    return center, r

def get_circle_coords(center, r):
    """Construct a circle by radius and center"""
    circle = [[r, 180* phi/3.14159265] for phi in range(0, 180, 5)]
    circle = [pol2cart(p[0], p[1]) + (center[0], center[1]) for p in circle]
    return circle

def orientIfSure(px, py, rx, ry, qx, qy):
    l = (ry - py) * (qx - px)
    r = (rx - px) * (qy - py)

    if (abs(l - r) >= 3.3306690738754716e-16 * abs(l + r)):
        return l - r
    else:
        return 0

# a more robust orientation test that's stable in a given triangle (to fix robustness issues)
def orient(rx, ry, qx, qy, px, py):
    return (orientIfSure(px, py, rx, ry, qx, qy) or\
        orientIfSure(rx, ry, qx, qy, px, py) or\
        orientIfSure(qx, qy, px, py, rx, ry)) < 0

def same_side(edge, p1, p2):
    """Check if points p1 and p2 are on the same side of edge"""
    x1, y1 = edge[0][0], edge[0][1]
    x2, y2 = edge[1][0], edge[1][1]
    ax, ay = p1[0], p1[1]
    bx, by = p2[0], p2[1]
    return orient(x1,y1, x2, y2, ax, ay) == orient(x1,y1, x2, y2, bx, by)

def get_distance(edge, center, r, candidate):
    """Distance from an edge to the other end of the circle.
     candidate indicates which side to read from"""
    p1, p2, p0 = edge[0], edge[1], center
    edge_len = norm([p2[0] - p1[0], p2[1] - p1[1]])
    sq = abs((p2[1]-p1[1])*p0[0] - (p2[0]-p1[0])*p0[1] + p2[0]*p1[1] - p2[1]*p1[0])
    dist = sq / edge_len
    if same_side(edge, center, candidate):
        return r + dist
    else:
        return r - dist

def point_in_arr(arr, point):
    """Are there points in the array"""
    for i in range(len(arr)):
        if arr[i][0] == point[0] and arr[i][1] == point[1]:
            return i
    return -1

def get_third_point(edge, triangles):
    """Get conjugate point for an edge from known triangles"""
    for triangle in triangles:
        i1, i2 = point_in_arr(triangle, edge[0]), point_in_arr(triangle, edge[1])
        if not (i1 == -1 or i2 == -1):
            for i in range(len(triangle)):
                if not (i1 == i or i2 == i):
                    return triangle[i]
    return None

def get_mate(edge, points, triangles):
    """Get a new mating point"""
    best_point, best_dist = None, None
#     points = reshuffle_points(points)
    third = get_third_point(edge, triangles)
    print(f"for edge: {edge}")
    print(f"ptsList: {points}")
    print(f" third point:{third}")
    for point in points:
        print(f"working on point: {point}")
        if point_in_arr(edge, point) > -1:
            print(f"exiting because point in arr: {point_in_arr(edge, point)}")
            continue
        if third is not None and same_side(edge, point, third):
            print(f"exiting: {point} in none or same side as {third}")
            continue
        center, r = get_circle(edge[0], edge[1], point)
        dist = get_distance(edge, center, r, point)
        print(f"  point: {point}\n  center: {center}\n   dist: {dist}")
        if best_point is None or dist < best_dist:
            best_point, best_dist = point, dist
    print(f"best : {best_point}")
    return best_point

def edge_in_frontier(frontier, edge):
    """Is there a rib in the border"""
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
    """Remove edge from boundary"""
    for i in range(len(frontier)):
        if frontier[i] == edge:
            frontier.remove(edge)
            break
    return frontier

def update_frontier(frontier, point, used_edge):
    """Refresh border"""
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
#         frontier = np.append(frontier, np.array([edge2]), axis=0)
        frontier.append(edge2)
    return frontier

def cart2pol(x, y):
    """Cartesian coordinates to polar"""
    r = sqrt(x**2 + y**2)
    φ = atan2(y, x)
    return(r, φ)

def norm(vector):
    t = 0
    for i in vector:
        t = t+i*i
    return sqrt(t)

def hull_edge(points):
    """First rib"""
#     points = reshuffle_points(points)
    p1 = points[0]
    for point in points:
        if point[1] < p1[1]:
            p1 = point
    p2 = points[0]
    min_angle = 3 * 3.14159265
    for point in points:
        if point == p1: continue
        vector = [point[0]-p1[0], point[1]-p1[1] ]
        angle = cart2pol(*vector)[1]
        if angle < min_angle:
            min_angle, p2 = angle, point
        elif angle == min_angle and norm(vector) > norm(p2 - p1):
            p2 = point
    return [p2, p1]

def delunay(points):
    triangles = []
    frontier = [hull_edge(points)]
    # hull_edges = convex_hull_recursive(points)
    # print(hull_edges)
    # frontier = [[hull_edges[0].x,hull_edges[0].y ], [hull_edges[1].x, hull_edges[0].y ]]
    print(frontier)
    # print(frontier[-1], frontier[:-1])
    while frontier:
        edge, frontier = frontier[-1], frontier[:-1]
        mate = get_mate(edge, frontier, triangles)
        if mate is not None:
            frontier = update_frontier(frontier, mate, edge)
            triangle = [edge[0], edge[1], mate]
            triangles.append(triangle)
    return triangles









if __name__ == "__main__":
    # points = [(0, 3),(2, 2),(1, 1),(2, 1),(3, 0),(0, 0),(3, 3),(2, -1),(2, -4),(1, -3)]
    points = [(1,2), (3,8), (6, 10), (7,5), (8,9)]

    # results_recursive = convex_hull_recursive(points)

    # print(results_recursive)

    pts = delunay(points)
    print(pts)



    # p = _validate_input(points)
    # e1 = Edge(p[0], p[1])
    # e2 = Edge(p[2], p[4])
    # e3 = Edge(p[1], p[2])
    # e4 = Edge(p[1], p[3])
    # t = Triangle(p[0], p[1], p[2])
    # val = e4.inTriangle(t)
    # # print(val)

    # hull_edges = convex_hull_recursive(points)
    # # print(hull_edges)
    # frontier = [Edge(hull_edges[0], hull_edges[-2])]
    # get_mate(e2, [e2,e3,e4], [Triangle(p[0],p[1],p[3])])
    # print(frontier)
