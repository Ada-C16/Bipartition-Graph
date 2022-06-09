# Can be used for BFS
from collections import deque 

def possible_bipartition(dislikes):
    """ Will return True or False if the given graph
        can be bipartitioned without neighboring nodes put
        into the same partition.
        Time Complexity: O(N+E) or O(V+E) #V for vertices
        Space Complexity: O(N)
    """
    if not dislikes:
        return True

    queue = deque()
    visited = set()

    red = set()
    green = set()

    if dislikes[0]:
        start_node = 0
    else:
        start_node = 1
    
    queue.append(start_node)
    visited.add(start_node)
    red.add(start_node)

    while len(queue) != 0:
        current = queue.popleft()
        
        for neighbor in dislikes[current]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
                if current in red:
                    green.add(neighbor)
                else:
                    red.add(neighbor)
            elif neighbor in visited:
                if current in red and neighbor in red:
                    return False
                if current in green and neighbor in green:
                    return False

    return True
    

