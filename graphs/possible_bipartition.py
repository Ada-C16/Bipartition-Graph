# Can be used for BFS
from collections import deque
from queue import Empty 

def possible_bipartition(dislikes):
    """ Will return True or False if the given graph
        can be bipartitioned without neighboring nodes put
        into the same partition.
        Time Complexity: ?
        Space Complexity: ?
    """

    dogs_to_see = deque()
    assigned_dogs = {}
    seen_dogs = set()

    for i in range(len(dislikes)):
        if dislikes[i] != []:
            dogs_to_see.append(i)
            break

    while dogs_to_see:
        current_dog = dogs_to_see.popleft()
        seen_dogs.add(current_dog)
        if current_dog not in assigned_dogs:
            assigned_dogs[current_dog] = "blue"
        
        current_dog_color = assigned_dogs[current_dog]

        for enemy in dislikes[current_dog]:
            if enemy in assigned_dogs and assigned_dogs[enemy] == current_dog_color:
                    return False
            else:
                assigned_dogs[enemy] = "red" if current_dog_color == "blue" else "blue"
                if enemy not in seen_dogs and enemy not in dogs_to_see:
                    dogs_to_see.append(enemy)
            
    return True


    



