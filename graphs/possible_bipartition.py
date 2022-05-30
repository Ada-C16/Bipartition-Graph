# Can be used for BFS
from collections import deque 

def possible_bipartition(dislikes):
    """ Will return True or False if the given graph
        can be bipartitioned without neighboring nodes put
        into the same partition.
        Time Complexity: ?
        Space Complexity: ?

        variation on a graph coloring problem
          - label dogs as group1 or group2

        dfs vs bfs
        - bfs, at each section, we can assign all children the other group
        - becuase "connections" are actually dogs that don't get along with one another
    
    Input: dislikes = [ [],
                        [2, 3],
                        [1, 4],
                        [1],
                        [2]
                    ]
    Output: true
    """
    if not dislikes:
        return True

    color_map = {}

    q = deque()
    q.append(1)
    color_map[1] = "group1"    
    """Input: dislikes = [ [],
                        [2, 3],     color_map = {
                        [1, 4],         1: "group1", 2: "group2",
                        [1],            3: "group2", 4: "group1"
                        [2]         
                    ]                  }
    Output: true
    q = {4}                      group_flag = -1
    current = 3                     group_id = "group2"
    children =  [1]          
    """
    while q:
        current = q.popleft()
        children = dislikes[current]

        # Assign children to group opposite of parents
        if color_map[current] == "group1":
            group_id = "group2"
        else:
            group_id = "group1"
        
        for child in children:
            if child in color_map:
                if color_map[child] != group_id:
                    return False
            # assign color to child
            else:    
                color_map[child] = group_id
                q.append(child)

    return True

