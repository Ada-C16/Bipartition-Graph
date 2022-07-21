# Can be used for BFS
from collections import deque

def possible_bipartition(dislikes):
    """ Will return True or False if the given graph
        can be bipartitioned without neighboring nodes put
        into the same partition.
        Time Complexity: O(n+e) number of nodes in the graph and e is the numbner of edges
        Space Complexity: O(n) storing 4 variables? Checked, G1, G2, queue. drop the constant
    """
    pass
    
    if not dislikes:
        return True

    # keep track of nodes checked
    # Create empty queue
    # add start_node (in this case 0) to queue
    checked = [None] * len(dislikes)
    queue = deque()
    queue.append(0)
    group1 = set()
    group2 = set()

    # So long as the queue is not empty, remove dog1
    # Mark that dog1 has been checked
    # if dog1 is not matched to a another hating ass dog, add the next dog to the queue
    while queue:
        current = queue.popleft()
        checked[current] = True
        if not dislikes[current]:
            queue.append(current + 1)

        # Loope through list of dogs. 
        # If current dog has NOT been checked
        # Add it to the queue to be assigned
        for dog in dislikes[current]:
            if not checked[dog]:
                queue.append(dog)
            
            # If current dog is not in group 1 and if the next dog is in group 2 
            # Then return false becuase there is no peaceful way to group these doggs.
            # But if the current dog is not in group 1 and the next dog is not in group 2
            # Then add the current dog to group 1
            if current not in group1:
                if dog in group2:
                    return False
                group1.add(dog)
        
            # Additionally, if the next dog is NOT group 1, add the current dog to group 2
            # But if the next dog is NOT in group 1 then add it to group 2
            else:
                if dog in group1:
                    return False
                group2.add(dog)
    return True
