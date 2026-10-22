# Practical 9 - Structural, automorphic (atomic) and regular equivalence


graph1 = {
    'A': ['B', 'C'],
    'B': ['A', 'D'],
    'C': ['A', 'D'],
    'D': ['B', 'C', 'E'],
    'E': ['D'],
}

graph2 = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['F', 'A', 'G'],
    'D': ['B'],
    'E': ['B'],
    'F': ['C'],
    'G': ['C'],
}

graph3 = {
    'A': ['B', 'C', 'H'],
    'B': ['A', 'D', 'E'],
    'C': ['F', 'A', 'G'],
    'D': ['B'],
    'E': ['B'],
    'F': ['C'],
    'G': ['C'],
    'H': ['A', 'I'],
    'I': ['H'],
}


def analyse(graph):
    # Degrees
    degree = {}
    for node in graph:
        degree[node] = len(graph[node])

    print("Degrees:")
    for node in graph:
        print(node, "-", degree[node])

    nodes = list(graph.keys())

    # Structural equivalence: exactly the same set of neighbours
    for i in range(len(nodes)):
        for j in range(i + 1, len(nodes)):
            a = nodes[i]
            b = nodes[j]
            if set(graph[a]) == set(graph[b]):
                print(a, "and", b, "are structurally equivalent")

    # Automorphic equivalence: same degree
    for i in range(len(nodes)):
        for j in range(i + 1, len(nodes)):
            a = nodes[i]
            b = nodes[j]
            if degree[a] == degree[b]:
                print(a, "and", b, "are automorphic equivalent")

    # Regular equivalence: neighbours have the same degree pattern
    for i in range(len(nodes)):
        for j in range(i + 1, len(nodes)):
            a = nodes[i]
            b = nodes[j]
            a_neighbour_degrees = sorted(degree[x] for x in graph[a])
            b_neighbour_degrees = sorted(degree[x] for x in graph[b])
            if a_neighbour_degrees == b_neighbour_degrees:
                print(a, "and", b, "are regularly equivalent")


for name, g in [("Graph 1", graph1), ("Graph 2", graph2), ("Graph 3", graph3)]:
    print("=" * 40)
    print(name)
    print("=" * 40)
    analyse(g)
    print()