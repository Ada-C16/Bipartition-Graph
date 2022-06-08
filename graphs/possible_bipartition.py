# Can be used for BFS
from collections import deque 

def possible_bipartition(dislikes):
    """ Will return True or False if the given graph
        can be bipartitioned without neighboring nodes put
        into the same partition.
        Time Complexity: O(N + E) where N = number of nodes (or puppies) and E = number of edges (or dislike relationships)
        Space Complexity: O(N)
    """
    
    if len(dislikes) <= 2:
        return True

    stack = []
    visited_and_parent = {}

    for n in range(len(dislikes)):
        if dislikes[n]!= []:
            stack.append(n)
            visited_and_parent[n] = None
            break
    
    while stack:
        current = stack.pop()
        for neighbor in dislikes[current]:
            if neighbor not in visited_and_parent:
                visited_and_parent[neighbor] = current
                stack.append(neighbor)
            elif neighbor in visited_and_parent and neighbor != visited_and_parent[current]:
                return False
    return True
