# Can be used for BFS
from collections import deque 

def possible_bipartition(dislikes):
    """ Will return True or False if the given graph
        can be bipartitioned without neighboring nodes put
        into the same partition.
        Time Complexity: O(V+E) v = vertices, e = edges
        Space Complexity: O(V+E)     
             O(V) to store array size V, then create an extra linked list object in case of a new edge, so  sum of linked lists’ sizes is equal to O(E), where E is the number of edges in graph
    """
    
    # definition:  A bipartite graph is a graph which all its nodes can be separated in two groups so that each element of one group is only related to elements of the other group-- two independent sets, u and v such that every edge connects a vertext in u to a vertex in v.  Can only have even edge length cycle -> no odd edge cycles result in bipartite graph. It’s also knows as bicolored graph (each group would represent a color, so every element in the graph is only related to another color element). 
    # Adjacency list stores only the neighbors of each node

    # if graph empty, return True
    if not dislikes:
        return True
   
    # create a queue to use bfs and hold the nodes
    # create a visited dictionary to keep track of visited nodes
    # add first index to q
    
    q = deque()
    q.append(0)
    visited = {}
    play_area_1 = []
    play_area_2 = []
    
    # assign puppies to play areas, return False if odd length cycle  
    # popleft() returns the element at the front of the queue and removes it from the queue 
   
    while q:
        #pop the first element in the queue 
        current_puppy = q.popleft()
        
        # mark node as visited
        visited[current_puppy] = True
        
        # if current node in dislikes doesn't have neighbor, add next index to q
        if not dislikes[current_puppy]:
            q.append(current_puppy + 1)
        
        # if current node in dislikes has neighor, determine if visited and assign to play area    
        for neighbor_puppy in dislikes[current_puppy]:
            
            if neighbor_puppy not in visited:
                visited[neighbor_puppy] = True
                q.append(neighbor_puppy)
                
            if current_puppy not in play_area_1:
                if neighbor_puppy in play_area_2:
                    return False
                play_area_1.append(neighbor_puppy)
            
            else:
                if neighbor_puppy in play_area_1:
                    return False
                play_area_2.append(neighbor_puppy)
    return True
                
                
                
                
                
                
                
                
                
                
                
                
                
        
    #     if current_puppy not in play_area_1 and current_puppy not in play_area_2:
    #         play_area_1.add(current_puppy)
        
    #     elif current_puppy in play_area_1:
    #         play_area_1.add(current_puppy)
        
    #     else:
    #         play_area_2.add(current_puppy)
            
    #     for neighbor_puppy in dislikes[current_puppy]:
    #         if neighbor_puppy not in play_area_1 and neighbor_puppy not in play_area_2:
    #             q.append(neighbor_puppy)
    #         if current_puppy not in play_area_1:
    #             play_area_1.add(neighbor_puppy)
    #             q.pop()
    #         elif current_puppy not in play_area_2:
    #             play_area_2.add(neighbor_puppy)
             
    #         else:
    #             return False
            