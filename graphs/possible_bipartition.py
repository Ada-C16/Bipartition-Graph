# Can be used for BFS
from collections import deque

def possible_bipartition(dislikes):
    """ Will return True or False if the given graph
        can be bipartitioned without neighboring nodes put
        into the same partition.
        Time Complexity: the worst, O(n^2)
        Space Complexity: O(n)
    """
    if len(dislikes) == 0:
        return True
    
    group1 = set()
    group1.add(0)
    group2 = set()
   
    q = deque()
    q.append(1) if len(dislikes[0]) == 0 else q.append(0)
    visited = {0}
      
    while q:
        current = q.popleft() 
        for neighbor in dislikes[current]:
            if current not in group1:
                group1.add(neighbor)
            elif current not in group2:
                group2.add(neighbor)
            if neighbor not in visited:
                q.append(neighbor)
                visited.add(neighbor)
    return len(group1) + len(group2) == len(dislikes)