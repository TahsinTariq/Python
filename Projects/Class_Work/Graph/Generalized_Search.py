import heapq

if __name__ == '__main__':
    print('Import this module to apply all four search in a general way. '
          'In itself, it does nothing ar all ¯\_(ツ)_/¯ ')


class Stack:
    def __init__(self):
        self.list = []

    def push(self, item):
        self.list.append(item)

    def pop(self):
        return self.list.pop()

    def isEmpty(self):
        return len(self.list) == 0


class Queue:
    def __init__(self):
        self.list = []

    def push(self, item):
        self.list.insert(0, item)

    def pop(self):
        return self.list.pop()

    def isEmpty(self):
        return len(self.list) == 0


class PriorityQueue:
    """
      Implements a priority queue data structure. Each inserted item
      has a priority associated with it and the client is usually interested
      in quick retrieval of the lowest-priority item in the queue. This
      data structure allows O(1) access to the lowest-priority item.
    """

    def __init__(self):
        self.heap = []
        self.count = 0

    def push(self, item, priority):
        entry = (priority, self.count, item)
        heapq.heappush(self.heap, entry)
        self.count += 1

    def pop(self):
        (_, _, item) = heapq.heappop(self.heap)
        return item

    def isEmpty(self):
        return len(self.heap) == 0

    def update(self, item, priority):
        for index, (p, c, i) in enumerate(self.heap):
            if i == item:
                if p <= priority:
                    break
                del self.heap[index]
                self.heap.append((priority, c, item))
                heapq.heapify(self.heap)
                break
        else:
            self.push(item, priority)


class PriorityQueueWithFunction(PriorityQueue):
    """
    Implements a priority queue with the same push/pop signature of the
    Queue and the Stack classes. This is designed for drop-in replacement for
    those two classes. The caller has to provide a priority function, which
    extracts each item's priority.
    """

    def __init__(self, priorityFunction):
        "priorityFunction (item) -> priority"
        self.priorityFunction = priorityFunction  # store the priority function
        PriorityQueue.__init__(self)  # super-class initializer

    def push(self, item):
        "Adds an item to the queue with priority from the priority function"
        PriorityQueue.push(self, item, self.priorityFunction(item))


class Node:
    def __init__(self, state, parent, child, pathCost=0, h=0):
        self.state = state
        self.parent = parent
        self.child = child
        self.pathCost = pathCost
        self.h = h


def backtrack(node):
    if (node.parent.state == 'None'):
        return []
    return backtrack(node.parent) + [node.parent.state]


def totalCost(node):
    return node.pathCost


def nullPath(*args):
    return [0]


def nullHeuristics(_):
    return 0


def generalSearch(Hash, structure, Start, End, path=nullPath, heuristics=nullHeuristics):
    visited = []
    structure.push(Node(Start, Node('None', None, None), Hash[Start], h=heuristics(Start)))
    while not structure.isEmpty():
        current = structure.pop()
        print(f'Searching {current.state} with a total cost of {current.pathCost + current.h}')
        if current.state == End:
            print(f"Found {current.state}")
            print(f"Number of Searched Nodes {len(visited)}")
            print(f"PathCost {totalCost(current)}")
            return backtrack(current)
        if current.state not in visited:
            visited.append(current.state)
            for i, kid in enumerate(current.child):
                if kid not in visited:
                    structure.push(Node(kid, current, Hash[kid],
                                        pathCost=current.pathCost + path(kid, current.state)[0],
                                        h=heuristics(kid)))
    # print('Not Found')
    return 'Not Found'
