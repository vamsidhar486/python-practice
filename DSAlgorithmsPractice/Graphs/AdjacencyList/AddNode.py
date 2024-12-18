from collections import deque

graph = {}


def add_vertex(v):
    """
    it works with any type of graph (directed, undirected and weighted)
    :param v:
    :return:
    """
    if v in graph:
        print(v, "is already present in the graph")
    else:
        graph[v] = []


def add_edge(v1, v2):
    """
    for undirected graph
    :param v1:
    :param v2:
    :return:
    """
    if v1 not in graph:
        print(v1, "is not present in the graph")
    elif v2 not in graph:
        print(v2, "is not present in the graph")
    else:
        graph[v1].append(v2)
        graph[v2].append(v1)


def DFS(node, graph):
    visited = [] # can be set, but it is unordered in python
    # for ordered set, use ordered_set module and import OrderedSet
    if node not in graph:
        print(node, "is not present in the graph")
        return
    stack = [node]
    while stack:  # this has to be performed till stack is empty
        current_node = stack.pop()  # default -1 for pop
        if current_node not in visited:
            visited.append(current_node)
        for node in graph[current_node]:
            if node not in visited:
                stack.append(node)

    return visited


def BFS(node, graph):
    visited = []
    if node not in graph:
        print(node, "is not present in the graph")
        return

    queue = deque()
    queue.append(node)

    while queue:  # this has to be performed till queue is empty
        current_node = queue.popleft()
        if current_node not in visited:
            visited.append( current_node)
        for node in graph[current_node]:
            if node not in visited:
                queue.append(node)

    return visited


add_vertex("A")
add_vertex("B")
add_vertex("C")
add_vertex("D")
add_vertex("E")
add_vertex("F")
add_vertex("G")
add_vertex("H")
add_vertex("I")
add_edge("A", "B")
add_edge("A", "C")
add_edge("B", "D")
add_edge("B", "E")
add_edge("D", "F")
add_edge("D", "G")
add_edge("C", "H")
add_edge("H", "I")


print(graph)
print(DFS("A", graph))
print(BFS("A", graph))