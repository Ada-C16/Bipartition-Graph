# Can be used for BFS
from collections import deque 

def possible_bipartition(dislikes):
    """ Will return True or False if the given graph
        can be bipartitioned without neighboring nodes put
        into the same partition.
        Time Complexity: O(N + E)
        Space Complexity: O(N)
    """

    if not dislikes:
        return True

    queue = deque()
    dogs = set()
    group_1 = set()
    group_2 = set()

    if dislikes[0]:
        start = 0
    else:
        start = 1

    queue.append(start)
    dogs.add(start)
    group_1.add(start)

    while len(queue):
        current = queue.popleft()

        for disliked_dog in dislikes[current]:
            if disliked_dog not in dogs:
                dogs.add(disliked_dog)
                queue.append(disliked_dog)
                if current in group_1:
                    group_2.add(disliked_dog)
                else:
                    group_1.add(disliked_dog)
            elif disliked_dog in dogs:
                if current in group_1 and disliked_dog in group_1:
                    return False
                elif current in group_2 and disliked_dog in group_2:
                    return False

    return True









