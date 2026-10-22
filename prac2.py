import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
#degree of each node in a graph
nodes=["A","B","C","D","E"]
edges=[("B","C"),("A","E"),("A","D"),("C","E"),("B","D")]

degrees = {node: 0 for node in nodes}
for edge in edges:
    degrees[edge[0]] += 1
    degrees[edge[1]] += 1   #0 for directed graph

print("Degree of each node:")
for node, degree in degrees.items():
    print(f"{node}: {degree}")

#Density
nodes = ['A','B','C','D','E']
adj_matrix = np.array([[0,1,1,1,0],
                      [1,0,1,0,1],
                      [1,1,0,1,0],
                      [1,0,1,0,0],
                      [0,1,0,0,0]])

n = len(nodes)

degrees = np.sum(adj_matrix, axis=1)
print("Degree of Graph")
for i in range(n):
    print(nodes[i], ":", degrees[i])

edges = np.sum(adj_matrix) // 2
density = (2 * edges) / (n * (n - 1))

print("\nDensity =", density)

edges = []

for i in range(len(nodes)):
    for j in range(i + 1, len(nodes)):

        if adj_matrix[i][j] == 1:
            edges.append((nodes[i], nodes[j]))

positions = {
    'A': (0, 2),
    'B': (2, 3),
    'C': (4, 2),
    'D': (2, 1),
    'E': (4, 0)
}

plt.figure(figsize=(7, 5))

# Draw edges
for u, v in edges:

    x1, y1 = positions[u]
    x2, y2 = positions[v]

    plt.plot(
        [x1, x2],
        [y1, y2],
        color='blue',
        linewidth=2
    )

# Draw nodes
for node in nodes:

    x, y = positions[node]

    plt.scatter(
        x, y,
        s=600,
        color='lightgreen',
        edgecolors='black'
    )

    plt.text(
        x, y,
        node,
        ha='center',
        va='center',
        fontsize=12,
        fontweight='bold'
    )

plt.title("Undirected Graph - Density")
plt.axis('off')
plt.show()

# Reciprocity using Adjacent Matrix

adj_matrix = [
    [0, 1, 0, 0],  # A points to B
    [1, 0, 1, 0],  # B points to A, C
    [0, 0, 0, 1],  # C points to D
    [0, 0, 1, 0]   # D points to C
]

total_links = 0
mutual_links = 0
n = len(adj_matrix)

for i in range(n):
    for j in range(n):
        if adj_matrix[i][j] == 1:
            total_links += 1

            if adj_matrix[j][i] == 1:
                mutual_links += 1


reciprocity = mutual_links / total_links if total_links > 0 else 0
print(f"Reciprocity: {reciprocity:.2f}")


#transtivity code using directed graph

n = ["a","b","c","d"]

adj_matrix = [[0,1,1,0],[0,0,0,0],[0,1,0,0],[0,0,1,0]]

closed = 0
open_triplets = 0

for i in range(len(n)):
    neighbours = []
    for j in range(len(n)):
        if adj_matrix[i][j] == 1:
            neighbours.append(j)

    for j in range(len(neighbours)):
        for k in range(j+1,len(neighbours)):
            if adj_matrix[neighbours[j]][neighbours[k]] == 0:
                open_triplets += 1
            else:
                 closed += 1

transtivity = closed/(closed+open_triplets)
print("Transtivity - Directed Graph :",transtivity)

nodes = ["a", "b", "c", "d"]

edges = []

for i in range(len(nodes)):
    for j in range(len(nodes)):

        if adj_matrix[i][j] == 1:
            edges.append((nodes[i], nodes[j]))

positions = {
    'a': (0, 2),
    'b': (4, 3),
    'c': (4, 1),
    'd': (0, 0)
}

plt.figure(figsize=(7, 5))

# Draw directed edges
for u, v in edges:

    x1, y1 = positions[u]
    x2, y2 = positions[v]

    plt.annotate(
        "",
        xy=(x2, y2),
        xytext=(x1, y1),
        arrowprops=dict(
            arrowstyle="->",
            color='blue',
            lw=2
        )
    )

# Draw nodes
for node in nodes:

    x, y = positions[node]

    plt.scatter(
        x, y,
        s=600,
        color='lightgreen',
        edgecolors='black'
    )

    plt.text(
        x, y,
        node,
        ha='center',
        va='center',
        fontsize=12,
        fontweight='bold'
    )

plt.title("Directed Graph - Transitivity")
plt.axis('off')
plt.show()
#transtivity code using undirected graph

n = ["a", "b", "c", "d"]
adj_matrix = [
    [0, 1, 1, 0],
    [1, 0, 1, 0],
    [1, 1, 0, 0],
    [0, 0, 0, 0]
]

closed = 0
open_triplets = 0

for i in range(len(n)):
    neighbours = []
    for j in range(len(n)):
        if adj_matrix[i][j] == 1:
            neighbours.append(j)

    for j in range(len(neighbours)):
        for k in range(j + 1, len(neighbours)):

            if adj_matrix[neighbours[j]][neighbours[k]] == 1 or adj_matrix[neighbours[k]][neighbours[j]] == 1:
                closed += 1
            else:
                open_triplets += 1


if (closed + open_triplets) > 0:
    transitivity = closed / (closed + open_triplets)
else:
    transitivity = 0.0

print(f"Closed Triangles: {closed}")
print(f"Open Triplets: {open_triplets}")
print(f"Transitivity - UnDirected Graph: {transitivity}")

edges = []

for i in range(len(n)):
    for j in range(i + 1, len(n)):

        if adj_matrix[i][j] == 1:
            edges.append((n[i], n[j]))

positions = {
    'a': (0, 2),
    'b': (3, 2),
    'c': (1.5, 0),
    'd': (4.5, 0)
}

plt.figure(figsize=(7, 5))

# Draw edges
for u, v in edges:

    x1, y1 = positions[u]
    x2, y2 = positions[v]

    plt.plot(
        [x1, x2],
        [y1, y2],
        color='blue',
        linewidth=2
    )

# Draw nodes
for node in nodes:

    x, y = positions[node]

    plt.scatter(
        x, y,
        s=600,
        color='lightgreen',
        edgecolors='black'
    )

    plt.text(
        x, y,
        node,
        ha='center',
        va='center',
        fontsize=12,
        fontweight='bold'
    )

plt.title("Undirected Graph - Transitivity")
plt.axis('off')
plt.show()

# local clustering coefficent
nodes = ["a", "b", "c", "d","e"]
adj_matrix = [
    [0,1,1,0,0],
    [1,0,1,0,0],
    [1,1,0,1,0],
    [0,0,1,0,1],
    [0,0,0,1,0]
]

size = len(nodes)

adj_squared = [[0] * size for _ in range(size)]
for i in range(size):
    for j in range(size):
        for k in range(size):
            adj_squared[i][j] += adj_matrix[i][k] * adj_matrix[k][j]

adj_cubed = [[0] * size for _ in range(size)]
for i in range(size):
    for j in range(size):
        for k in range(size):
            adj_cubed[i][j] += adj_squared[i][k] * adj_matrix[k][j]

for i in range(size):
    k_i = sum(adj_matrix[i])
    E_i = adj_cubed[i][i] // 2

    if k_i < 2:
        c_i = 0.0
    else:
        c_i = (2 * E_i) / (k_i * (k_i - 1))

    print(f"Node {nodes[i]}:  local clustering coefficient = {c_i:.2f}")


edges = []

for i in range(len(nodes)):
    for j in range(i + 1, len(nodes)):

        if adj_matrix[i][j] == 1:
            edges.append((nodes[i], nodes[j]))

positions = {
    'a': (0, 2),
    'b': (2, 3),
    'c': (4, 2),
    'd': (6, 1),
    'e': (4, 0)
}

plt.figure(figsize=(8, 5))

# Draw edges
for u, v in edges:

    x1, y1 = positions[u]
    x2, y2 = positions[v]

    plt.plot(
        [x1, x2],
        [y1, y2],
        color='blue',
        linewidth=2
    )

# Draw nodes
for node in nodes:

    x, y = positions[node]

    plt.scatter(
        x, y,
        s=600,
        color='lightgreen',
        edgecolors='black'
    )

    plt.text(
        x, y,
        node,
        ha='center',
        va='center',
        fontsize=12,
        fontweight='bold'
    )

plt.title("Undirected Graph - Local Clustering Coefficient")
plt.axis('off')
plt.show()