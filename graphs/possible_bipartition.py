# Can be used for BFS
from collections import deque


def possible_bipartition(dislikes):
    """Will return True or False if the given graph
    can be bipartitioned without neighboring nodes put
    into the same partition.
    Time Complexity: ?
    Space Complexity: ?
    """

    if not dislikes:
        return True

    groups = [None] * len(dislikes)
    group_1 = 0
    group_2 = 1
    start_dog = 0
    while start_dog < len(dislikes) and not dislikes[start_dog]:
        start_dog += 1

    groups[start_dog] = group_1
    queue = deque()
    queue.append(start_dog)
    while queue:
        curr_dog = queue.popleft()
        for disliked_dog in dislikes[curr_dog]:
            if groups[disliked_dog] is None:
                groups[disliked_dog] = (
                    group_1 if groups[curr_dog] == group_1 else group_2
                )
                queue.append(disliked_dog)
            elif groups[disliked_dog] == groups[curr_dog]:
                return False
    return True
