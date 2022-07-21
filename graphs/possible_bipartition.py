from collections import deque


def possible_bipartition(dislikes):
    """ Will return True or False if the given graph
        can be bipartitioned without neighboring nodes put
        into the same partition.
        Time Complexity: O(n * m) where n is the number of nodes/dogs 
        and m is the number of edges
        Space Complexity: O(n)
    """
    # PART 1: CREATE AN ADJACENCY LIST
    def createGraph(nodes):
        graph = {}
        for index, edge in enumerate(nodes):
            graph[index] = []
            for neighbor in edge:
                graph[index].append(neighbor)
        return graph

    graph = createGraph(dislikes)

    visited = {}

    for i in range(len(dislikes)):
        if i not in visited:
            queue  = deque([(i, 1)])
            while queue:
                dog, group = queue.popleft()
                if dog in visited:
                    if group == visited[dog]:
                        continue
                    else:
                        return False
                visited[dog] = group

                for dog_enemy_neighbor in graph[dog]:
                    queue.append((dog_enemy_neighbor, group * (-1)))
        # print(visited)
    return True

