# Can be used for BFS
from collections import deque
import queue 

def possible_bipartition(dislikes):
    """ Will return True or False if the given graph
        can be bipartitioned without neighboring nodes put
        into the same partition.
        Time Complexity: ?
        Space Complexity: ?
    """
    if not dislikes:
        True

    pack = {}
    dogque = deque()

    for dog in range(len(dislikes)):
        if dog not in pack:
            dogque += [dog]
            pack[dog] = 0

        while dogque:
            doggy_node = dogque.popleft()
            for neighbor in dislikes[doggy_node]:
                if neighbor not in pack:
                    dogque += [neighbor]
                    pack[neighbor] = pack[doggy_node] ^ 1
                elif pack[neighbor] == pack[doggy_node]:
                    return False
    return True