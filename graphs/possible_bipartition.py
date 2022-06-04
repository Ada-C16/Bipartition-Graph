# Can be used for BFS
from collections import deque 

def possible_bipartition(dislikes):
    """ Will return True or False if the given graph
        can be bipartitioned without neighboring nodes put
        into the same partition.
        Time Complexity: ?
        Space Complexity: ?
    """
    '''
    They can be partitioned if there are no cycles
    OR if there are no odd numbered cycles
    STEPS:
        do depth first search looking for cycles
            like regular depth first exept you store what the return value is
            if it has something that has been seen before that's not the return value
            Then it's a cycle!

    OR maybe I can just traverse either putting it in A or B, if I run into an issue then false
    DFS 
    UNION OF SETS - NOPE, go back to looking for loops
    '''
    

    
            

def bfs(dislikes):
    q = deque()
    visited_nodes = set()
    for i in range(len(dislikes)):  
        if i not in visited_nodes:
        # doing this to get any islands, without going through the whole thing unnecessarily
            q.append(i)
            while len(q) > 0:
                current = q.popleft()
                visited_nodes.add(current)
                for node in dislikes[current]:
                    if node not in visited_nodes:
                        q.append(node)
    return visited_nodes


def dfs(dislikes):
    visited = set()
    for i in range(len(dislikes)):
        if i not in visited:
            dfs_helper(dislikes, visited, i)

def dfs_helper(dislikes, visited, current):
    if current in visited:
        return
    else:
        visited.add(current)
        for node in dislikes[current]:
            dfs_helper(dislikes, visited, node)

def find_cycle(dislikes):
    all_visited_nodes = set()
    q = deque()
    for i in range(len(dislikes)):
        visited_nodes_this_cycle = set()
        if i not in all_visited_nodes:
            q.append(i)
            while len(q) > 0:
                current = q.popleft()
                all_visited_nodes.add(current)
                visited_nodes_this_cycle.add(current)
                for node in dislikes[current]:
                    if node not in all_visited_nodes:
                        q.append(node)
                    elif node in visited_nodes_this_cycle and current not in dislikes[node]:
                        return True
    return False





