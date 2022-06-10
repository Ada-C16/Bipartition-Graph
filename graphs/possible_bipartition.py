# Can be used for BFS
from collections import deque 

def possible_bipartition(dislikes):
    """ Will return True or False if the given graph
        can be bipartitioned without neighboring nodes put
        into the same partition.
        Time Complexity: O(n+e) # n is number of nodes, e is number of edges
        Space Complexity: O(n)
    """
    # 0, 1, -1
    number_puppies = len(dislikes)    
    color_list = [0] * (number_puppies)
        
    def check_color(cur_node, cur_color, parent_color):
        # base case
        if color_list[cur_node] != 0:
            if color_list[cur_node] != parent_color:
                return True
            if color_list[cur_node] == parent_color:
                return False


        # recursive case  # cur_node's color is 0
        color_list[cur_node] = cur_color
        adj_list = dislikes[cur_node]
        for neigbor in adj_list:
            if check_color(neigbor, -cur_color, cur_color) == False:
                return False
        return True
    
    for cur_node in range(number_puppies):
        res = check_color(cur_node, 1, 0)
        if res == False:
            return False
    return True

