# Can be used for BFS
from collections import deque 
from collections import defaultdict

def possible_bipartition(dislikes):
    """ Will return True or False if the given graph
        can be bipartitioned without neighboring nodes put
        into the same partition.
        Time Complexity: 0(N+E)
        Space Complexity: O(N)
    """
    grouped = {}
    dog_q=deque()
    for i in range(len(dislikes)):
        if i not in grouped:
            dog_q += [i]
            grouped[i] = 0
        
        while dog_q:
            dog_node = dog_q.popleft()
            for neighbor in dislikes[dog_node]:
                if neighbor not in grouped:
                    dog_q+=[neighbor]
                    grouped[neighbor] = grouped[dog_node] ^ 1
                elif grouped[neighbor] == grouped[dog_node]:
                    return False
    return True





