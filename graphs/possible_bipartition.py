# Can be used for BFS
import collections 
from queue import Queue

def possible_bipartition(dislikes):
    """ 
    Given a set of N puppies (numbered 0, 1, 2, ..., N - 1), we would like to split
    them into two groups of any size to use two play areas.

    Some dogs have a history of fighting with specific other dogs and shouldn't 
    be put into the same play area.

    Formally, if dislikes[i] = [a, b], it means dog i is not allowed to 
    put in the same group as dog a or dog b.

    Return true if and only if it is possible to split the dogs into
    two groups where no fighting will occur.

    ### Example 1

    ```
    Input: dislikes = [ [],
                [2, 3],
                [1, 4],
                [1],
                [2]
                ]
    Output: true
```

Explanation: group1 [0, 1, 4], group2 [2, 3]
        group 1     group 2
            0           2
            1           3
            4
    
    #  all items within the same set should be disjoint
    #  A bipartite graph can only have  even edge length cycle.
    #
    
    Will return True or False if the given graph
        can be bipartitioned without neighboring nodes put
        into the same partition.
        Time Complexity: O(n) or O(v + E)
        Space Complexity: O(n)
    """

    # each edge should be different collors 

    if len(dislikes) == 0:
        return True

    graph = {}
    graph_items = len(dislikes)
    for node in range(graph_items):
        edge = dislikes[node]
        graph[node] = edge 
    print(graph)
    # BFS -> loop thorugh each item and check if items are enemies 

    
    def bfs(queue, is_visited, node):
        queue.put((node,0))
        while not queue.empty():
            curr, value = queue.get()
            if curr not in is_visited:
                is_visited[curr] =0
            # for the neighbours
            for next_node in graph[curr]:
                if next_node not in is_visited:
                    new_visited = value ^ 1
                    is_visited[next_node] = new_visited
                    queue.put((next_node, new_visited))
                else:
                    # check if it is in the same group
                    if  is_visited[curr] == is_visited[next_node]:
                        # they are  supposed to be in different groups 
                        return False
        return True

    queue = Queue()
    is_visited = {}
    for node in range(graph_items):
        if not bfs(queue, is_visited, node):
            return False
    return True
