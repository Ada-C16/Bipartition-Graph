# Can be used for BFS
from collections import deque 

def possible_bipartition(dislikes):
    """ Will return True or False if the given graph
        can be bipartitioned without neighboring nodes put
        into the same partition.
        Time Complexity: O(N + E)
        Space Complexity: O(N)
    """
    group_map = {}

    if not dislikes:
        return True

    first_dog = 0
    for i in range(len(dislikes)):
        if dislikes[i]:
            first_dog = i
            break
    
    # BFS
    q = deque()
    q.append(first_dog)
    group_map[first_dog] = "group1"

    while q:
        current_dog = q.popleft()
        enemies = dislikes[current_dog]

        if group_map[current_dog] == "group1":
            current_group_id = "group2"
        else:
            current_group_id = "group1"

        for enemy in enemies:
            if enemy in group_map:
                if group_map[enemy] != current_group_id:
                    return False
            else:
                group_map[enemy] = current_group_id
                q.append(enemy)

    return True


