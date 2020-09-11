l = 0.9

UP = (0, -1)
DOWN = (0, 1)
LEFT = (-1, 0)
RIGHT = (1, 0)
actions = [UP, DOWN, LEFT, RIGHT]

addT = lambda a: sum(a)
def addTuple(t1,t2):
    return tuple(map(addT, zip(t1,t2)))

def bellman(T, current, l, side):
    return T * (0 + l * side)