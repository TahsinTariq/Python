from math import sqrt, atan2

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
    #r = norm(center - a)
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
    while frontier:
        edge, frontier = frontier[-1], frontier[:-1]
        mate = get_mate(edge, points, triangles)
        if mate is not None:
            frontier = update_frontier(frontier, mate, edge)
            triangle = [edge[0], edge[1], mate]
            triangles.append(triangle)
    return triangles









if __name__ == "__main__":
    points = [(1,2), (3,8), (6, 10), (7,5), (8,9)]

    pts = delunay(points)

    print(pts)
