# Can be used for BFS
from collections import deque 

def possible_bipartition(dislikes):
    """ Will return True or False if the given graph
        can be bipartitioned without neighboring nodes put
        into the same partition.
        Time Complexity: O(N+E) N-number of nodes, E -number of edges
        Space Complexity: O(N)??
    """
    if not dislikes:
        return True

    queue = deque()
    visited = set()
    group1 = set()
    group2 = set()

    queue.append(0)

    while queue:
        current = queue.popleft()
        for neigbor_dog in dislikes[current]:
            if neigbor_dog not in visited:
                visited.add(neigbor_dog)
                queue.append(neigbor_dog)
                if current in group1:
                    group2.add(neigbor_dog)
                else:
                    group1.add(neigbor_dog)
            elif neigbor_dog in visited:
                if current in group1 and neigbor_dog in group1:
                    return False
                if current in group2 and neigbor_dog in group2:
                    return False

    return True
