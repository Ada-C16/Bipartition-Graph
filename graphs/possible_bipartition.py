# Can be used for BFS
from collections import deque 

def possible_bipartition(dislikes):
    """ Will return True or False if the given graph
        can be bipartitioned without neighboring nodes put
        into the same partition.
        Time Complexity: ?
        Space Complexity: ?
    """
    queue = deque()
    set_a = set()
    set_b = set()
    visited = set()

    if not dislikes:
        return True
    if dislikes[0]:
        starting_node = 0
    else:
        starting_node = 1
    
    queue.append(starting_node)
    visited.add(starting_node)
    set_a.add(starting_node)

    while len(queue) > 0:
        node = queue.popleft()
        for i in dislikes[node]:
            if i not in visited:
                queue.append(i)
                visited.add(i)
                if node in set_a:
                    set_b.add(i)
                else:
                    set_a.add(i)
            else:
                if node in set_a and i in set_a or node in set_b and i in set_b:
                    return False
    
    return True

