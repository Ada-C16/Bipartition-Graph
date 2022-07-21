# Can be used for BFS
from collections import deque 

def possible_bipartition(dislikes):
    """ Will return True or False if the given graph
        can be bipartitioned without neighboring nodes put
        into the same partition.
        Time Complexity: O(N+E)
        Space Complexity: O(N)
    """
    visited_dogs = set()

    if len(dislikes) == 0:
        return True

    def dfs(node, parent=None):

        if node in visited_dogs:
            return False
        visited_dogs.add(node)

        for dog in dislikes[node]:
            if dog != parent:
                no_cycle = dfs(dog, node)
                if not no_cycle:
                    return False

        return True

    for dog in range(len(dislikes)):
        if dog not in visited_dogs:
            no_cycle = dfs(dog)
            if not no_cycle:
                return False
    return True

