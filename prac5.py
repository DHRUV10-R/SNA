#Dijkstra Shortest Path, Density and the Ego Node
import numpy as np
import matplotlib.pyplot as plt
from collections import deque

# New adjacency matrix
adj = np.array([
    [0, 1, 1, 0, 0, 0],
    [1, 0, 1, 1, 0, 0],
    [1, 1, 0, 0, 1, 0],
    [0, 1, 0, 0, 1, 1],
    [0, 0, 1, 1, 0, 1],
    [0, 0, 0, 1, 1, 0]
])

print("Adjacency Matrix:")
print(adj)


# BFS to find shortest path length
def bfs(adj, s, t):
    q = deque([(s, 0)])
    seen = {s}

    while q:
        v, d = q.popleft()

        if v == t:
            return d

        for u in range(len(adj)):
            if adj[v][u] == 1 and u not in seen:
                seen.add(u)
                q.append((u, d + 1))

    return -1


# Find shortest path length from node 0 to node 5
shortest_path = bfs(adj, 0, 5)
print("\nShortest path length:", shortest_path)


# Graph density
n = len(adj)
edges_count = np.sum(adj) / 2
density = (2 * edges_count) / (n * (n - 1))

print("Graph density:", density)


# Find node with most connections (Ego node)
degrees = np.sum(adj, axis=1)
ego = np.argmax(degrees)

print("Node degrees:", degrees)
print("Ego node:", ego)


# Extract graph edges
edges = []

for i in range(len(adj)):
    for j in range(i + 1, len(adj)):
        if adj[i][j] == 1:
            edges.append((i, j))


# New node positions
pos = {
    0: (0, 2),
    1: (1, 3),
    2: (2, 2),
    3: (1, 1),
    4: (3, 1),
    5: (3, 3)
}


# Draw sociogram
plt.figure(figsize=(7, 5))

for node, (x, y) in pos.items():
    if node == ego:
        color = "red"
        size = 800
    else:
        color = "skyblue"
        size = 500

    plt.scatter(
        x, y,
        s=size,
        color=color,
        edgecolors="black",
        zorder=2
    )

    plt.text(
        x, y, str(node),
        ha="center",
        va="center",
        fontsize=10,
        zorder=3
    )


# Draw edges
for a, b in edges:
    x1, y1 = pos[a]
    x2, y2 = pos[b]

    plt.plot(
        [x1, x2],
        [y1, y2],
        "k-",
        linewidth=1,
        zorder=1
    )


plt.title("Sociogram - New Network")
plt.axis("off")
plt.tight_layout()
plt.show()