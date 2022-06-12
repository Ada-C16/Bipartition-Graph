def possible_bipartition(dislikes):
    """ Will return True or False if the given graph
        can be bipartitioned without neighboring nodes put
        into the same partition.
        Time Complexity: O(E)
        Space Complexity: O(E)
    """
    visited = set()

    l = len(dislikes)

    if l == 0:
        return True

    def dfs(node, parent=None):

        if node in visited:
            return False
        visited.add(node)
        
        for enemy in dislikes[node]:
            if enemy != parent:
                has_no_cycle = dfs(enemy, node)
                if not has_no_cycle:
                    return False
        
        return True

    for dog in range(l):
        if dog not in visited:
            has_no_cycle = dfs(dog)
            if not has_no_cycle:
                return False
    return True


