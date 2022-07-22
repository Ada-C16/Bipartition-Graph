# Can be used for BFS
from collections import deque 

def possible_bipartition(dislikes):
    """ Will return True or False if the given graph
        can be bipartitioned without neighboring nodes put
        into the same partition.
        Time Complexity: O(n)
        Space Complexity: O(n)
    """
    
    if not dislikes:
        return True

    deck = deque()
    visited = set()
    left = set()
    right = set()

    if dislikes[0]:
        start = 0
    else:
        start = 1
    
  
    deck.append(start)
    visited.add(start)
    left.add(start)


    while len(deck) != 0:
        current = deck.popleft()
        
        for enemy in dislikes[current]:
            
            if enemy not in visited:
                visited.add(enemy)
                deck.append(enemy)
            
                if current in left:
                    right.add(enemy)
                else:
                    left.add(enemy)

          
            elif enemy in visited:
                if current in left and enemy in left:
                    return False
                if current in right and enemy in right:
                    return False

    return True
