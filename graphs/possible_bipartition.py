# Can be used for BFS
from collections import deque 

def possible_bipartition(dislikes):
    """ Will return True or False if the given graph
        can be bipartitioned without neighboring nodes put
        into the same partition.
        Time Complexity: O(n+e)
        Space Complexity: O(n)
    """
    if not dislikes:
        return True

    tracked = [False] * len(dislikes)
    gargy_a = set()
    gargy_b = set()

    q = deque()
    q.append(0)

    while q:
        current = q.popleft()
        tracked[current] = True        
        if not dislikes[current]:
            q.append(current+1)

        for gargoyle in dislikes[current]:
            if not tracked[gargoyle]:              
                q.append(gargoyle)

            if current not in gargy_a:
                if gargoyle in gargy_b:
                    return False
                gargy_a.add(gargoyle)    
            else:
                if gargoyle in gargy_a:
                    return False
                gargy_b.add(gargoyle)    
    
    return True