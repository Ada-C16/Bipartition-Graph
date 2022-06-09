from collections import defaultdict  

def possible_bipartition(dislikes):
    """ Will return True or False if the given graph
        can be bipartitioned without neighboring nodes put
        into the same partition.
        Time Complexity: O(V+E)
        Space Complexity: O(V+E)
    """
    # create a hash where dogs will be assigned to group 1 or group -1
    grouped = {}
    
    for dog in range(len(dislikes)): 
        if dog not in grouped:
            grouped[dog] = 1
        # do BFS 
        queue = [dog]  
        while queue:
            curr_dog = queue.pop(0)  
            for enemy in dislikes[curr_dog]:
                if enemy not in grouped:
                    # make dog's group diff from what its enemy dog's group was
                    grouped[enemy] = -grouped[curr_dog]
                    # add it to queue so BFS traversal can continue 
                    queue.append(enemy)
                # if you find two enemy dogs that were assigned the same group, 
                # return False 
                elif grouped[curr_dog] == grouped[enemy]:
                    return False 
    
    # if you made it to end w/o finding two enemies in same group, return True 
    return True 