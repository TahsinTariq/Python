import heapq

if __name__ == '__main__':
    print('Import this module to apply dfs, bfs, ucs or a* search. '
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
    def __init__(self, state, parent, child, actionTaken, stepCost, pathCost, h=0):
        self.state = state
        self.parent = parent
        self.child = child
        self.actionTaken = actionTaken
        self.stepCost = stepCost
        self.pathCost = pathCost
        self.h = h


def backtrack(node):
    if (node.parent == 'None'):
        return []
    return backtrack(node.parent) + [node.parent.state]


def dfs(Hash):
    visited = []
    stack = Stack()
    stack.push(Node('S', 'None', Hash['S'], 'None', 0, 0))
    while not stack.isEmpty():
        current = stack.pop()
        print('Searching : ' + str(current.state))
        if current.state == 'G':
            print('Found G')
            # print(visited)
            return backtrack(current)
        for kid in current.child:
            if kid not in visited:
                stack.push(Node(kid, current, Hash[kid], 'None', 0, 0))
                visited.append(kid)
    print('Not found')


def bfs(Hash):
    visited = []
    queue = Queue()
    queue.push(Node('S', 'None', Hash['S'], 'None', 0, 0))
    while not queue.isEmpty():
        current = queue.pop()
        print('Searching : ' + str(current.state))
        if current.state == 'G':
            print('Found G')
            # print(visited)
            return backtrack(current)
        for kid in current.child:
            if kid not in visited:
                queue.push(Node(kid, current, Hash[kid], 'None', 0, 0))
                visited.append(kid)
    print('Not found')


def totalCost(node):
    return node.pathCost


def ucs(Hash):
    visited = []
    pq = PriorityQueue()
    pq.push(Node('S', 'None', [i[0] for i in Hash['S']], [i[1] for i in Hash['S']], 0, 0), 0)
    while not pq.isEmpty():
        current = pq.pop()
        print(f'Searching {current.state}')
        if current.state == 'G':
            print(f'Found {current.state}')
            print(f"PathCost {totalCost(current)}")
            return backtrack(current)
        if current.state not in visited:
            visited.append(current.state)
            for kid, cost in zip(current.child, current.actionTaken):
                if kid not in visited:
                    pq.push(Node(kid, current, [i[0] for i in Hash[kid]], [i[1] for i in Hash[kid]],
                                 1, cost + current.pathCost), cost + current.pathCost)
    print('Not found')


def astar(Hash, pq):
    visited = []
    pq.push(Node('Arad', 'None', [i[0] for i in Hash['Arad']], [i[1] for i in Hash['Arad']], 0, 0))
    while not pq.isEmpty():
        current = pq.pop()
        # print(f"Expanding node {current.state}")
        if current.state == 'Bucharest':
            print(f'Found {current.state}')
            print(f"PathCost {totalCost(current)}")
            return backtrack(current)
        if current.state not in visited:
            visited.append(current.state)
            for kid, cost in zip(current.child, current.actionTaken):
                if kid not in visited:
                    pq.push(Node(kid, current, [i[0] for i in Hash[kid]], [i[1] for i in Hash[kid]],
                                 1, cost + current.pathCost))
    print('Not found')
