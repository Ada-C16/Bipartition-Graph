# Can be used for BFS
from collections import deque
from collections import defaultdict

def possible_bipartition(dislikes: list[list[int]]):
    """ Will return True or False if the given graph
        can be bipartitioned without neighboring nodes put
        into the same partition.
        Time Complexity: O(N + E) where N is the number of nodes (dogs) and E is the number of edges (likes/dislikes).
        Space Complexity: O(N) where N is the number of nodes (dogs).
    """
    group_assignment = {i: None for i in range(len(dislikes))}

    # dfs recursively

    def dfs(node, group):
        # if node has no group, assign node to group that was passed as argument
        if not group_assignment[node]:
            group_assignment[node] = group
        else:
            return group_assignment[node] == group

        for dog in dislikes[node]:
            if not dfs(dog, 2 if group == 1 else 1):
                return False
        return True

    for i in range(len(dislikes)):
        if not group_assignment[i] and not dfs(i, 1):
            return False

    return True


