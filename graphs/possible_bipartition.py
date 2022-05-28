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
        #make adjacency list
        # use colors to determine if odd or even length cycle
        # use bfs (queue) to determine if bipartite

    #if graph empty, return True
    if not dislikes:
        return True
   
    # create a queue to use bfs and hold the nodes
    q = deque()
    play_area_1 = set()
    play_area_2 = set()
     
    for node in range(len(dislikes)):
        q.append(node)
    
    
    # assign puppies to play areas and return False if there is an odd length cycle  
    # popleft() returns the element at the front of the queue and removes it from the queue 
    while q:
        current_puppy = q.popleft()
        
        if not dislikes[current_puppy]:
            q.append(current_puppy + 1)
        
        if current_puppy not in play_area_1 and current_puppy not in play_area_2:
            play_area_1.add(current_puppy)
        
        elif current_puppy in play_area_1:
            play_area_1.add(current_puppy)
        
        else:
            play_area_2.add(current_puppy)
            
        for neighbor_puppy in dislikes[current_puppy]:
            if neighbor_puppy not in play_area_1 and neighbor_puppy not in play_area_2:
                q.append(neighbor_puppy)
            if current_puppy not in play_area_1:
                play_area_1.add(neighbor_puppy)
                q.pop()
            elif current_puppy not in play_area_2:
                play_area_2.add(neighbor_puppy)
             
            else:
                return False
            
        
        

            

