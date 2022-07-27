# Can be used for BFS
from collections import deque
from dis import dis 

def possible_bipartition(dislikes):
    """ Will return True or False if the given graph
        can be bipartitioned without neighboring nodes put
        into the same partition.
        Time Complexity: O(n)
        Space Complexity: O(n)
    """
    if not dislikes:
        return True

    seen = {}
    for dog in range(len(dislikes)):
        seen[dog] = False

    q = deque()
    play_area1 = set()
    play_area2 = set()

    first_dog = None
    for clash in dislikes:
        if len(clash) > 0:
            first_dog = clash[0]
            break
  
    play_area1.add(first_dog)
    q.appendleft(first_dog)
    seen[first_dog] = True

    while q:
        main_dog = q.pop()
        for other_dog in dislikes[main_dog]:
            if seen[other_dog] == False:
                q.appendleft(other_dog)
                seen[other_dog] = True
                if main_dog in play_area1:
                    play_area2.add(other_dog)
                else:
                    play_area1.add(other_dog)
            elif seen[other_dog] == True:
                if set([main_dog, other_dog]).issubset(play_area1):
                    return False
                if set([main_dog, other_dog]).issubset(play_area2):
                    return False

    return True

