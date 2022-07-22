# Can be used for BFS
from collections import deque 

def possible_bipartition(dislikes):
    """ Will return True or False if the given graph
        can be bipartitioned without neighboring nodes put
        into the same partition.
        Time Complexity: O(VE)
        Space Complexity: O(N)
        Input: dislikes = [ [],
                    [2, 3],
                    [1, 4],
                    [1],
                    [2]
                  ]
        Output: true
    """
    # breadth first search means looking at all of the neighbors of a node first
    # can use a hashmap/adjacency matrix to better identify the vertex and edges
    # can use a set to keep track of what has been visited
    # and another set to keep track of the two groups?
    # if a vertex has been visited, continue?
    # if a vertex has not been visited, add it's neighbors to the opposite group
    # at the end, see if the current vertex and neighbors are in same group. return false
    # if a node has been visited and the neighbor has also been visited, it is not possible to bipartition them?
    if dislikes == []:
        return True
    else:
        queue = deque()
        visited = set()
        group1 = set()
        group2 = set()


        queue.append(0) # have to start at 0 
        visited.add(0)
        group1.add(0)    
        
        while len(queue) > 0:
            current = queue.popleft()
            if dislikes[current] == []: # guard clause to prevent error if vertex is empty
                current += 1
                queue.append(current)
            for edge in dislikes[current]:
                if edge not in visited:
                    visited.add(edge)
                    queue.append(edge)
                    if current in group1:
                        group2.add(edge)
                    else:
                        group1.add(edge)
                elif edge in visited:
                    if current in group1 and edge in group1:
                        return False
                    elif current in group2 and edge in group2:
                        return False

        return True
        



    


