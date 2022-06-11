# Can be used for BFS
from collections import deque 

def possible_bipartition(dislikes):
    """ Will return True or False if the given graph
        can be bipartitioned without neighboring nodes put
        into the same partition.
        N = Nodes + E = Edges
        Time Complexity: O(N + E)
        Space Complexity: O(N)

    """
    # color dict stores bool values
    color = {}
    for node in range(len(dislikes)):
        if node not in color:
            stack = [node]
            color[node] = 0
            while stack:
                node = stack.pop()
                for neighbor in dislikes[node]:
                    if neighbor not in color:
                        stack.append(neighbor)
                        color[neighbor] = not(color[node])
                    elif color[neighbor] == color[node]:
                        return False
    return True







