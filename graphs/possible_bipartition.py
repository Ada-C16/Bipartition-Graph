# Can be used for BFS
from collections import deque

def possible_bipartition(dislikes):
    """ Will return True or False if the given graph
        can be bipartitioned without neighboring nodes put
        into the same partition.
        Time Complexity: O(N)
        Space Complexity: O(NE)
    """
    if not dislikes:
        return True

    # find first non empty array ex: [[], [2,3], [1,3], [1,2]]
    start_dog = 0
    for dog in range(len(dislikes)):
        if dislikes[dog]:
            start_dog = dog
            break

    visited_dogs = set()
    visited_dogs.add(start_dog)
    group1 = []
    group2 = []

    # dogs to visit
    q = deque()
    q.append(start_dog)

    # while q is not None
    # current is left dog
    # if current not in visited, add to q
    # if current not in group1 or group2, add to group1
    # if current not in group 1 and dislikes not in group1, add to group2, otherwise return False
    # Else, if current not in group 2 and dislikes not in group2, add to group1, otherwaise return False


    while q:
        current_dog = q.popleft()
        visited_dogs.add(current_dog)
        if current_dog not in group1 and current_dog not in group2:
            group1.append(current_dog)
        for disliked_dog in dislikes[current_dog]:
            if disliked_dog not in visited_dogs:
                q.append(disliked_dog)

            if current_dog in group1:
                if disliked_dog in group1:
                    return False
                group2.append(disliked_dog)
            else:
                if disliked_dog in group2:
                    return False
                group1.append(disliked_dog)

    return True
