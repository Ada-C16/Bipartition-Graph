# Can be used for BFS
from collections import deque 

def possible_bipartition(dislikes):
    # get the first dog that has dislikes, if there are none, return True
    first = None
    for i in range(len(dislikes)):
        if dislikes[i]:
            first = i
            break
    if first == None:
        return True

    # initialize queue, two dog pens, add the first dog to the queue and assign it to pen_a
    q = deque()
    pen_a = set()
    pen_b = set()
    q.append((first, "pen_a"))

    while len(q) > 0:
        # current = q.popleft() # breadth first
        current = q.pop() # depth first - they both work
        dog = current[0]
        assigned_pen_name = current[1]

        friendly_pen = pen_a if assigned_pen_name == "pen_a" else pen_b
        enemy_pen = pen_b if assigned_pen_name == "pen_a" else pen_a
        enemy_pen_name = "pen_b" if assigned_pen_name == "pen_a" else "pen_a"

        # if current is in one pen and assigned to the other pen, return False
        # if current is in one pen and assigned to that pen, do nothing
        # otherwise, current is a new dog, so add it to its assigned pen and add its 
        # dislikes to the que with the opposite assigned pen
        if dog in enemy_pen:
            return False
        elif dog in friendly_pen:
            continue
        else:
            friendly_pen.add(dog)
            for dog in dislikes[dog]:
                q.append((dog, enemy_pen_name))

    return True