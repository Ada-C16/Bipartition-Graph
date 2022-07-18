# Can be used for BFS
from collections import deque 

def possible_bipartition(dislikes):
    """ Will return True or False if the given graph
        can be bipartitioned without neighboring nodes put
        into the same partition.
        Time Complexity: O(V + E)
        Space Complexity: O(n)
    """
    if not dislikes:
        return True
    
    groups = [None] * len(dislikes)
    queue = deque()
    first_group = 0
    second_group = 1
    first_dog = 0
    for i in  range(len(dislikes)):
        if dislikes[i]:
            first_dog = i
            break
        if first_dog == None:
            return True
    queue.append(first_dog)
    groups[first_dog] = first_group
    groups[first_dog] = True

    while queue:
        curr_dog = queue.popleft()
        for i in dislikes[curr_dog]:
            if groups[i] is None:
                groups[i] = first_group if groups[curr_dog] else second_group
                queue.append(i)
            elif groups[i] == groups[curr_dog]:
                return False
    return True