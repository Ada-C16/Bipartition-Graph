# Can be used for BFS
from collections import deque 

def possible_bipartition(dislikes):
    """ Will return True or False if the given graph
        can be bipartitioned without neighboring nodes put
        into the same partition.
        Time Complexity: ?
        Space Complexity: ?
    """
    pen_1 = []
    pen_2 = []

    for puppy in dislikes:
        if puppy in pen_1 or puppy in pen_2:
            continue
        pen_1.append(puppy)

        puppy_queue = []
        for puppy_rival in puppy:
            puppy_queue.append(dislikes[puppy_rival])
        while puppy_queue:
            current_puppy = puppy_queue.pop(0)

            for puppy_rival in current_puppy:
                if dislikes[puppy_rival] in pen_1:
                    if current_puppy in pen_1:
                        return False
                    else:
                        if current_puppy not in pen_2:
                            pen_2.append(current_puppy)
                elif dislikes[puppy_rival] in pen_2:
                    if current_puppy in pen_2:
                        return False
                    else:
                        if current_puppy not in pen_1:
                            pen_1.append(current_puppy)
                else:
                    puppy_queue.append(dislikes[puppy_rival])
    return True
