"""
Creating graph
"""

nodes = []
graph = []
node_count = 0


def add_node(v):
    """
    for any type of graph, adding node/vertex would be same
    :param v:
    :return:
    """
    global node_count
    if v in nodes:
        print(v, "Node is already present in graph")
    else:
        node_count += 1
        nodes.append(v)
        for n in graph:
            n.append(0)
        temp = []
        for i in range(node_count):
            temp.append(0)
        graph.append(temp)


def delete_node(v):
    global node_count
    if v not in nodes:
        print(v, "node is not present in graph")
    else:
        i1 = nodes.index(v)
        node_count -= 1
        nodes.remove(v)
        graph.pop(i1)   # remove row
        for i in graph:  # remove column
            i.pop(i1)


"""
adding edge is for connectivity, we have to be careful about the type of graph
directed, undirected and weighted
"""

def add_edge(v1, v2):
    """
    for undirected graph
    :param v1:
    :param v2:
    :return:
    """
    if v1 not in nodes:
        print(v1, "is not present in the graph")
    elif v2 not in nodes:
        print(v2, "is not present in the graph")
    else:
        i1 = nodes.index(v1)
        i2 = nodes.index(v2)
        graph[i1][i2] = 1
        graph[i2][i1] = 1


def add_edge(v1, v2):
    """
    for directed graph
    :param v1:
    :param v2:
    :return:
    """
    if v1 not in nodes:
        print(v1, "is not present in the graph")
    elif v2 not in nodes:
        print(v2, "is not present in the graph")
    else:
        i1 = nodes.index(v1)
        i2 = nodes.index(v2)
        graph[i1][i2] = 1


def add_edge(v1, v2, cost):
    """
    For undirected weighted graph
    :param v1:
    :param v2:
    :param cost:
    :return:
    """
    if v1 not in nodes:
        print(v1, "is not present in the graph")
    elif v2 not in nodes:
        print(v2, "is not present in the graph")
    else:
        i1 = nodes.index(v1)
        i2 = nodes.index(v2)
        graph[i1][i2] = cost
        graph[i2][i1] = cost


def add_edge(v1, v2, cost):
    """
    For directed weighted graph
    :param v1:
    :param v2:
    :param cost:
    :return:
    """
    if v1 not in nodes:
        print(v1, "is not present in the graph")
    elif v2 not in nodes:
        print(v2, "is not present in the graph")
    else:
        i1 = nodes.index(v1)
        i2 = nodes.index(v2)
        graph[i1][i2] = cost

def delete_edge(v1,v2):
    """
    undirected and weighted graph
    :param v1:
    :param v2:
    :return:
    """
    if v1 not in nodes:
        print(v1, "node is not present in the graph")
    elif v2 not in nodes:
        print(v2, "node is not present in the graph")
    else:
        i1 = nodes.index(v1)
        i2 = nodes.index(v2)
        graph[i1][i2] = 0
        graph[i2][i1] = 0


def delete_edge(v1,v2):
    """
    for directed and directed weighted graph
    :param v1:
    :param v2:
    :return:
    """
    if v1 not in nodes:
        print(v1, "node is not present in the graph")
    elif v2 not in nodes:
        print(v2, "node is not present in the graph")
    else:
        i1 = nodes.index(v1)
        i2 = nodes.index(v2)
        graph[i1][i2] = 0

def print_graph():
    for i in range(node_count):
        for j in range(node_count):
            print(graph[i][j], end=" ")
        print()


add_node("A")
print(nodes)
print(graph)
add_node("B")
add_edge("A", "B", 5)
print(nodes)
print(graph)
add_node("C")
add_edge("B", "C", 10)
print(nodes)
delete_node("C")
print(graph)
print_graph()
