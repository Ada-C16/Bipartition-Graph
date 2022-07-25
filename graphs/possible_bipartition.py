# Can be used for BFS
from collections import deque 

# def possible_bipartition(dislikes):
#     """ Will return True or False if the given graph
#         can be bipartitioned without neighboring nodes put
#         into the same partition.
#         Time Complexity: O(n+e)
#         Space Complexity: O(n)
#     """

def possible_bipartition(dislikes):
    visited = [-1] * (len(dislikes))
    
    for i in range(1, len(dislikes)):
        if visited[i] == -1 and  len(dislikes[i]) > 0:
            if not visit(0, i, dislikes, visited):
                return False
            
    return True

def visit(curLevel, i, dislikes, visited):     
    if visited[i] >= 0:
        return (curLevel - visited[i]) % 2 == 0
            
    visited[i] = curLevel
    for des in dislikes[i]:
        if not visit(curLevel + 1, des, dislikes, visited):
            return False
    return True