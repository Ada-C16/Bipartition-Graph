# Can be used for BFS
from collections import deque

def possible_bipartition(dislikes):
    """ Will return True or False if the given graph
        can be bipartitioned without neighboring nodes put
        into the same partition.
        Time Complexity: O(N + E) where n = number of dogs and e = number of edges/dislikes between dogs
        Space Complexity: O(N) where n = number of dogs
    """
    if not dislikes:
        return True

    groups = [None] * len(dislikes)
    GROUP_A = 0
    GROUP_B = 1
    start_dog = 0
    # find first dog with dislikes
    while start_dog < len(dislikes) and not dislikes[start_dog]:
        start_dog += 1

    groups[start_dog] = GROUP_A
    queue = deque()
    queue.append(start_dog)
    while queue:
        curr_dog = queue.popleft()
        for disliked_dog in dislikes[curr_dog]:
            # case: never seen this dog before
            if groups[disliked_dog] is None:
                # assign it to its group
                groups[disliked_dog] = GROUP_A if groups[curr_dog] == GROUP_B else GROUP_B
                queue.append(disliked_dog)
            elif groups[disliked_dog] == groups[curr_dog]:
                # graph can't be bipartitioned
                return False
    return True







