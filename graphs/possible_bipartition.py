# Can be used for BFS
from collections import deque

def possible_bipartition(dislikes):
    """ Will return True or False if the given graph
        can be bipartitioned without neighboring nodes put
        into the same partition.
        Time Complexity: O(N+E) - each node and each edge will be explored
        Space Complexity: O(N) - worst case - need to add each node to the Queue
    """
    if not dislikes:
        return True

    first = 0
    for dog in range(len(dislikes)):
        if dislikes[dog]:
            first = dog
            break

    checked_dogs = set()
    checked_dogs.add(first)
    group_a = []
    group_b = []

    q = deque()
    q.append(first)

    while q:
        current = q.popleft()
        checked_dogs.add(current)
        if current not in group_a and current not in group_b:
            group_a.append(current)
        for solo_dog in dislikes[current]:
            if solo_dog not in checked_dogs:
                q.append(solo_dog)

            if current in group_a:
                if solo_dog in group_a:
                    return False
                group_b.append(solo_dog)
            else:
                if solo_dog in group_b:
                    return False
                group_a.append(solo_dog)

    return True
