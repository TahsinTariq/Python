# from Class_Work.Graph import Search
import Search
# from Class_Work.Intro_to_AI.Graph.Generalized_Search import *
# from .Post_Graph import First_try_of_A_star

Hash = {}
# with open('graph_to_test_Unweighted', 'r') as file:
#         for line in file:
#             sen = line.split()
#             if not sen[0].isdigit():
#                 Hash[sen[0]] = sen[1:]
# print(Hash)
# print(dfs(Hash))
# print(bfs(Hash))


with open('graph_to_test_Weighted', 'r') as file:
    for line in file:
        sen = line.split()
        if not sen[0].isdigit():
            temp = []
            for i in range(len(sen[1::2])):
                temp += [(sen[2*i+1], int(sen[2*i+2]))]
            Hash[sen[0]] = temp
print(Hash)
print(Search.ucs(Hash))


# h = {}
# with open('E:\Programme outputs\Python\Projects\Class_Work\Post_Graph\Romanian_roadmap', 'r') as file:
#     for line in file:
#         sen = line.split()
#         if not sen[0].isdigit():
#             temp = []
#             h[sen[0]] = int(sen[1])
#             for i in range(len(sen[2::2])):
#                 temp += [(sen[2 * i + 2], int(sen[2 * i + 3]))]
#             Hash[sen[0]] = temp
# print(Hash)
# print(h)
# pq = PriorityQueueWithFunction(lambda node: h[node.state]+node.pathCost)
# print(astar(Hash, pq))

'''
    For bfs and dfs:
    make a Hash where the keys are the nodes
    and the values are a list of all neighbours of that Node
'''
# with open('graph_to_test_Unweighted', 'r') as file:
#         for line in file:
#             sen = line.split()
#             if not sen[0].isdigit():
#                 Hash[sen[0]] = sen[1:]
# print(Hash)
# # structure = Stack()
# structure = Queue()
# print(generalSearch(Hash, structure, 'S', 'G'))

'''
    For ucs:
    make a Hash similar to bfs, dfs
    Make another similar Hash that contains the cost of each neighbour of that Node
    Make sure to maintain the order of the two Hash
'''
# step = {}
# step['None'] = []
# with open('graph_to_test_Weighted', 'r') as file:
#     for line in file:
#         sen = line.split()
#         if not sen[0].isdigit():
#             temp = []
#             for i in range(len(sen[1::2])):
#                 temp += [(sen[2*i+1], int(sen[2*i+2]))]
#             Hash[sen[0]] = [i[0] for i in temp]
#             step[sen[0]] = [i[1] for i in temp]
# print(Hash)
# print(step)
# structure = PriorityQueueWithFunction(lambda node : node.pathCost)
# function = lambda x,prev: [step[prev][i] for i in range(len(Hash[prev])) if Hash[prev][i] == x]
# print(generalSearch(Hash, structure, 'S', 'G', path =function ))
# a = function('e','S')
# print(int(a[0]))


'''
    For A*:
    Everything similar to ucs
    Make another Hash. This one contains the heuristics value of each node to the goal
    In case of different search problems: make a function that generates the heuristics be it a normal one or lambda
'''

# step = {}
# h = {}
# step['None'] = []
# with open('E:\Programme outputs\Python\Projects\Class_Work\Post_Graph\Romanian_roadmap', 'r') as file:
#     for line in file:
#         sen = line.split()
#         if not sen[0].isdigit():
#             temp = []
#             h[sen[0]] = int(sen[1])
#             for i in range(len(sen[2::2])):
#                 temp += [(sen[2*i+2], int(sen[2*i+3]))]
#             Hash[sen[0]] = [i[0] for i in temp]
#             step[sen[0]] = [i[1] for i in temp]
# print(Hash)
# print(step)
# print(h)
# structure = PriorityQueueWithFunction(lambda node : node.pathCost + h[node.state])
# function = lambda x,prev: [step[prev][i] for i in range(len(Hash[prev])) if Hash[prev][i] == x]
# heuristicsFunction = lambda x: h[x]
# print(generalSearch(Hash, structure, 'Arad', 'Bucharest', path = function, heuristics = heuristicsFunction ))
