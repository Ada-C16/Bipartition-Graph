from collections import deque, defaultdict

def possible_bipartition(dislikes):
    """ Will return True or False if the given graph
        can be bipartitioned without neighboring nodes put
        into the same partition.
        Time Complexity: ?
        Space Complexity: ?
    """
    dislike_graph={}
    n= len(dislikes)

    for item in dislikes:
        dislike_graph[dislikes.index(item)]= item


    groupings=[0 for _ in range(n)]

    def group_dogs(dog, dislike_graph, groupings, group =1):
        if groupings[dog]:
            return True
        groupings[dog] = group

        for dislike in dislike_graph[dog]:
            if groupings[dog]== groupings[dislike]:
                return False
            if not group_dogs(dislike,dislike_graph, groupings, -group):
                return False
        return True
    
    for dog in dislike_graph:
        if groupings[dog]:
            continue
        if not group_dogs(dog,dislike_graph, groupings):
            return False
    return True




