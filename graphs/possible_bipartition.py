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
    for i in range(len(dislikes)):
        dislikes[i].append(i)
        dog_queue.append(dislikes[i])

    while len(dog_queue) != 0:
    # Assign dog to check to current_dog
        current_dog = dog_queue.popleft()

        if len(kennel_a) == 0:
            kennel_a.append(current_dog.pop())
        elif len(kennel_a) > 0 and len(kennel_b) == 0:
            kennel_b.append(current_dog)
        else:
            for dog in kennel_a:
                if current_dog[0] != dog and current_dog[1] != dog:
                    kennel_a.append(current_dog)
                    break
        # elif len(kennel_b) == 0:
        #     kennel_b.append(current_dog)
        if len(kennel_b) > 0:
            for dog in kennel_b:
                if current_dog[0] != dog and current_dog[1] != dog:
                    kennel_b.append(current_dog)
        else:
            return False

    return True

