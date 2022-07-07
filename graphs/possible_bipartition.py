# Can be used for BFS
from collections import deque 

def possible_bipartition(dislikes):
    """ Will return True or False if the given graph
        can be bipartitioned without neighboring nodes put
        into the same partition.
        Time Complexity: ?
        Space Complexity: ?
    """
    # Create an empty queue
    dog_queue = deque()
    kennel_a = []
    kennel_b = []

    # Add dogs to the queue
    for dog in dislikes:
        dog_queue.append(dog)

    while len(dog_queue) != 0:
    # Assign dog to check to current_dog
        current_dog = dog_queue.pop()

        if current_dog not in kennel_a:
            kennel_a.append(current_dog)
        elif current_dog not in kennel_b:
            kennel_b.append(current_dog)
        else:
            return False

    return True

