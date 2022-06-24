# Can be used for BFS
from queue import Queue

def possible_bipartition(dislikes):
    """ Will return True or False if the given graph
        can be bipartitioned without neighboring nodes put
        into the same partition.
        Time Complexity: ?
        Space Complexity: ?
    """
    # Time Complexity: O(n)
    # Space Complexity: O(n)
    
    if not dislikes:
        return True
    
    adj_list = {}
    for i in range(len(dislikes)):
        adj_list[i] = dislikes[i]
                
    colors = {}
    for pair in dislikes:
        for num in pair:
            if num not in colors:
                colors[num] = -1

    for i in range(len(dislikes)):
        if dislikes[i]:
            break
    
    src = dislikes[i][0]
    q = Queue()
    q.put(src)
    colors[src] = 1
    while not q.empty():
        current = q.get()
        color = 1 - colors[current]
        for v in adj_list[current]:
            if colors[v] == -1:
                colors[v] = color
                q.put(v)
            elif colors[v] == colors[current]:
                print("colors", colors)
                return False
    return True

