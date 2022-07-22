# Can be used for BFS
from collections import deque 
import queue

def possible_bipartition(dislikes):
    """ Will return True or False if the given graph
        can be bipartitioned without neighboring nodes put
        into the same partition.
        Time Complexity: O(N+E)
        Space Complexity: O(N+E)
    """



    if not dislikes:
        return True 

    group = {}
    dog_que = deque()

    for dog in range(len(dislikes)):
        if dog not in group:
            dog_que += [dog]
            group[dog] = 0
        while dog_que:
            node = dog_que.popleft()
            for other_dog in dislikes[node]:
                if other_dog not in group:
                    dog_que += [other_dog]
                    group[other_dog] = group[node] ^ 1
                elif group[other_dog] == group[node]:
                    return False 

    return True