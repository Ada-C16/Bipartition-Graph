# Can be used for BFS
from collections import deque 

color_list = ["blue, orange"]


def dfs(dislikes, current_node, graph, current_color):
    neighbors = dislikes[current_node]
    next_color = (current_color + 1) % len(color_list)

    for neighbor in neighbors:
        color = graph.get(neighbor)

        if not color:
            graph[neighbor] = color_list[next_color]
            if not dfs(dislikes=dislikes, current_node=neighbor, graph=graph, current_color=next_color):
                return False
        elif color != color_list[next_color]:
            return False

    return True

def possible_bipartition(dislikes):
    """ Will return True or False if the given graph
        can be bipartitioned without neighboring nodes put
        into the same partition.
        Time Complexity: ?
        Space Complexity: ?
    """
    graph = {}
    current_color = 0

    for node in range(len(dislikes)):
        if not graph.get(node):
            graph[node] = color_list[current_color]

            if not dfs(dislikes=dislikes, current_node=node, graph=graph, current_color=current_color):
                return False
    return True

