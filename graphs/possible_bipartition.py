# Can be used for BFS
from collections import deque
from queue import Queue 

def possible_bipartition(dislikes):
    """ Will return True or False if the given graph
        can be bipartitioned without neighboring nodes put
        into the same partition.
        Time Complexity: 2*O(E*N) or O(E*N)
        Space Complexity: 3*O(n) or O(n)
        dislikes = [ [],
                [2, 3],
                [1, 4],
                [1],
                [2]
            ]
    """

    if not dislikes:
        return True
    
    to_pet = deque() # O(n)
    pet_dogs = set() # O(n)
    playpen_1 = set() # O(n)
    playpen_2 = set() # O(1) if above is O(n)
    
    # Find the first dog with dog rivals ... O(E N)
    for dog in range(len(dislikes)):
        if to_pet:
            break
        if not dislikes[dog]:
            pet_dogs.add(dog)
        if dog:
            for each_disliked_dog in dislikes[dog]:
                to_pet.append(each_disliked_dog)

    # Now iterate through to_pet list
    while to_pet: 
        doggie = to_pet.popleft()

        # Add each dog to pet_dogs or seen
        pet_dogs.add(doggie)

        # if dog has not already in playpen, put in playpen 1
        if doggie not in playpen_1 and doggie not in playpen_2:
            playpen_1.add(doggie)

        # for each dog's rivals
        for disliked_dog in dislikes[doggie]:
            # check if the rivak dog has already been pet, if it hasn't add to queue
            if disliked_dog not in pet_dogs:
                to_pet.append(disliked_dog)
            
            # check if dog rivals have ended up in same playpen, return false if so
            # otherwise put dog in opposite playpen
            if doggie in playpen_1:
                if disliked_dog in playpen_1:
                    return False
                playpen_2.add(disliked_dog)
            else:
                if disliked_dog in playpen_2:
                    return False
                playpen_1.add(disliked_dog)

    return True
