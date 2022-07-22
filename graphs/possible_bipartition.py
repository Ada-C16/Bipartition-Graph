# Can be used for BFS
from collections import deque 

def possible_bipartition(dislikes):
    """ Will return True or False if the given graph
        can be bipartitioned without neighboring nodes put
        into the same partition.
        Time Complexity: O(n^2)
        Space Complexity: O(n)
    """
    # Create an empty queue
    dog_queue = deque()
    kennel_a = []
    kennel_b = []

    # Add dogs to the queue
    for i in range(len(dislikes)):
        dog_queue.append(dislikes[i])

    while len(dog_queue) != 0:
    # Assign dog to check to current_dog
        current_dog_dislikes = dog_queue.popleft()
        current_dog = dislikes.index(current_dog_dislikes)

        if len(current_dog_dislikes) == 0:
            kennel_a.append(current_dog)
        else:
            for i in range(len(current_dog_dislikes)-1):
                if current_dog_dislikes[i] not in kennel_a:
                    kennel_a.append(current_dog)
                elif current_dog_dislikes[i] not in kennel_b:
                    kennel_b.append(current_dog)
                else:
                    return False
    
    return True