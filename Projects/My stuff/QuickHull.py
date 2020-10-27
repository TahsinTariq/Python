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

    def __repr__(self):
        return f"({self.x}, {self.y})"

    def __hash__(self):
        return hash(self.x)


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




def main():
    points = [
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
    points = [(0,0), (0,2), (2,0), (1,3), (3,1)]
    results_recursive = convex_hull_recursive(points)
    print(results_recursive)


if __name__ == "__main__":
    main()
