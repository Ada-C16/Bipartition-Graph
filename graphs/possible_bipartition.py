from collections import defaultdict  

def possible_bipartition(dislikes):
    """ Will return True or False if the given graph
        can be bipartitioned without neighboring nodes put
        into the same partition.
        Time Complexity: O(V+E)
        Space Complexity: O(V+E)
    """
    # create an adjacency list to represent the graph
    graph = defaultdict(list)
    for dislike in dislikes:
        # if there are no enemies, no need to add to graph
        if len(dislike) > 1:
            dog, enemy = dislike[0], dislike[1]
            graph[dog].append(enemy)
        # if there are 3 or more dogs who fight each other, 
        # you can't divide the non-fighters into just 2 groups,
        # so return False immediately 
        if len(dislike) > 2:
            return False 
    
    # create a hash where dogs will be assigned to group 1 or group -1
    grouped = {}
    
    for dog in range(len(graph)):
        if dog not in grouped:
            grouped[dog] = 1
        # do BFS 
        queue = [dog]
        while queue:
            curr_dog = queue.pop(0)
            for enemy in graph[curr_dog]:
                if enemy not in grouped:
                    # make dog's group diff from what its enemy dog's group was
                    grouped[enemy] = -grouped[curr_dog]
                    # add it to queue so BFS traversal can continue 
                    queue.append(enemy)
                # if you find two enemy dogs that were assigned same group, 
                # return False 
                elif grouped[curr_dog] == grouped[enemy]:
                    return False 
    
    # if you made it to end w/o finding two enemies in same group, return True 
    return True 

