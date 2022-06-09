# Can be used for BFS
from collections import deque 

""" Will return True or False if the given graph
        can be bipartitioned without neighboring nodes put
        into the same partition.
        Time Complexity: O(N + E)
        Space Complexity: O(N)

        variation on a graph coloring problem
          - label dogs as group1 or group2

        dfs vs bfs
        - bfs, at each section, we can assign all children the other group
        - becuase "connections" are actually dogs that don't get along with one another
    
    Input: dislikes = [ (0) [],                
                        (1) [2, 3],
                        (2) [1, 4],
                        (3) [1],
                        (4) [2]
                    ]
    Output: true

    Input: dislikes = [ [],
                        [2, 3],     group_map = {
                        [1, 4],         1: "group1", 2: "group2",
                        [1],            3: "group2", 4: "group1"
                        [2]         
                    ]                  }
    Output: true
    q = {4}                      group_flag = -1
    current = 3                     group_id = "group2"
    children =  [1]          
"""

def possible_bipartition(dislikes):
    if not dislikes:
        return True

    # Find first non-empty dislikes list
    # For edge case: dislikes = [ [], [], [3,4], [2,4], [2,3] ]
    first_dog = 0
    for index in range(len(dislikes)):
        if dislikes[index]:
            first_dog = index
            break

    group_map = {}  # { 1: "group1", 2: "group2" }

    q = deque()
    q.append(first_dog)
    group_map[first_dog] = "group1"    
    
    while q:
        current_dog = q.popleft()
        enemies = dislikes[current_dog]

        # Assign children to group opposite of parents
        if group_map[current_dog] == "group1":
            current_group_id = "group2"
        else:
            current_group_id = "group1"
        
        for enemy in enemies:
            if enemy in group_map:
                if group_map[enemy] != current_group_id:
                    return False
            # assign color to child
            else:    
                group_map[enemy] = current_group_id
                q.append(enemy)

    return True

