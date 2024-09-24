import collections

"""

"""

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


def add_edge(v1, v2):
    """
    for directed graph
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


def add_edge(v1, v2, cost):
    """
    for undirected weighted graph
    :param v1:
    :param v2:
    :return:
    """
    if v1 not in graph:
        print(v1, "is not present in the graph")
    elif v2 not in graph:
        print(v2, "is not present in the graph")
    else:
        graph[v1].append([v2, cost])
        graph[v2].append([v1, cost])


def add_edge(v1, v2, cost):
    """
    for directed weighted graph
    :param v1:
    :param v2:
    :return:
    """
    if v1 not in graph:
        print(v1, "is not present in the graph")
    elif v2 not in graph:
        print(v2, "is not present in the graph")
    else:
        graph[v1].append([v2, cost])


def delete_node(v):
    """
    works for directed/undirected graph
    :param v:
    :return:
    """
    if v not in graph:
        print(v, "node is not present in graph")
    else:
        graph.pop(v)  # remove row
        for i in graph:  # removing column
            list1 = graph[i]
            if v in list1:
                list1.remove(i)


def delete_node(v):
    """
    for weighted graph
    :param v:
    :return:
    """
    if v not in graph:
        print(v, "node is not present in graph")
    else:
        graph.pop(v)  # remove row
        for i in graph:  # removing column
            list1 = graph[i]
            for j in list1:
                if v == j[0]:
                    list1.remove(j)
                    break


def delete_edge(v1, v2):
    """
    for undirected graph
    :param v1:
    :param v2:
    :return:
    """
    if v1 not in graph:
        print(v1, "node is not present in graph")
    elif v2 not in graph:
        print(v2, "node is not present in graph")
    else:
        graph[v1].remove(v2)
        graph[v2].remove(v1)


def delete_edge(v1, v2):
    """
    for directed graph
    :param v1:
    :param v2:
    :return:
    """
    if v1 not in graph:
        print(v1, "node is not present in graph")
    elif v2 not in graph:
        print(v2, "node is not present in graph")
    else:
        graph[v1].remove(v2)


def delete_edge(v1, v2, cost):
    """
    for un directed weighted graph
    :param v1:
    :param v2:
    :param cost:
    :return:
    """
    if v1 not in graph:
        print(v1, "node is not present in graph")
    elif v2 not in graph:
        print(v2, "node is not present in graph")
    else:
        graph[v1].remove([v2, cost])
        graph[v2].remove([v1, cost])


def delete_edge(v1, v2, cost):
    """
    for un directed weighted graph
    :param v1:
    :param v2:
    :param cost:
    :return:
    """
    if v1 not in graph:
        print(v1, "node is not present in graph")
    elif v2 not in graph:
        print(v2, "node is not present in graph")
    else:
        graph[v1].remove([v2, cost])


# visited = set()
#
#
# def DFS(node, visited, graph):
#     if node not in graph:
#         print(node, "not present in the graph")
#         return
#     if node not in visited:
#         visited.add(node)
#         for i in graph[node]:
#             DFS(i, visited, graph)  # for weighted graph i[0]


def DFS(node, graph):
    visited = set()
    if node not in graph:
        print(node, "is not present in the graph")
        return
    stack = []
    while stack:  # this has to be performed till stack is empty
        current_node = stack.pop()  # default -1 for pop
        if current_node not in visited:
            visited.add(current_node)
        for i in graph[current_node]:
            stack.append(i)

    return visited

def BFS(node, graph):
    visited = set()
    if node not in graph:
        print(node, "is not present in the graph")
        return
    else:
        visited.add(node)
    queue = collections.deque[node]
    while queue:  # this has to be performed till queue is empty
        current_node = queue.popleft()
        for i in graph[current_node]:
            if i not in visited:
                visited.add(i)
                queue.append(i)
    return visited


add_vertex("A")
print(graph)
add_vertex("A")
add_vertex("B")
add_vertex("C")
add_vertex("D")
add_vertex("E")
add_edge("A", "B", 10)
add_edge("C", "D", "1")
print(graph)
print(DFS("A", graph))
# BFS("A", graph)
