# Can be used for BFS
from collections import deque 

def possible_bipartition(dislikes):
    """ Will return True or False if the given graph
        can be bipartitioned without neighboring nodes put
        into the same partition.
        Time Complexity: O(n)
        Space Complexity: O(n)
    """
    
    # Ensure there are dislikes to begin with
    if not dislikes:
        return True

    # Set empty deck, visited set, and two teams
    deck = deque()
    visited = set()
    left = set()
    right = set()

    # # If 0 has no dislikes, start with 1
    if dislikes[0]:
        start = 0
    else:
        start = 1
    
    # Starting search at index 0, 
    # it will start out as visited
    # and on the left team
    deck.append(start)
    visited.add(start)
    left.add(start)

    # If we get to the end of the search and the deck is empty, base case True
    while len(deck) != 0:
        current = deck.popleft()
        
        for enemy in dislikes[current]:
            
            if enemy not in visited:
                visited.add(enemy)
                # Add this dog to our search
                deck.append(enemy)
                
                # If the current dog is in the left, add him to the right / vice-versa
                if current in left:
                    right.add(enemy)
                else:
                    left.add(enemy)

            # This enemy has been visited before and thus is on a team 
            # so find out what team he is on and make sure he is not 
            # on a team with the current dog
            elif enemy in visited:
                if current in left and enemy in left:
                    return False
                if current in right and enemy in right:
                    return False

    return True