#Graph is Bipartite Using Two Colours
import matplotlib.pyplot as plt

graph = {
    1: [4, 8, 2],
    2: [1, 7, 3],
    3: [2, 4, 6],
    4: [1, 3, 5],
    5: [4, 6, 8],
    6: [3, 5, 7],
    7: [2, 6, 8],
    8: [1, 7, 5]
}

color = {
    1: 'B', 2: 'Y', 3: 'B', 4: 'Y',
    5: 'B', 6: 'Y', 7: 'B', 8: 'Y'
}

def bipartite(graph, color):
    for i in graph:
        for j in graph[i]:
            if color[i] == color[j]:
                print(f"Edge ({i},{j}) has same color.")
                return False
    return True

print("Given Graph is Bipartite:", bipartite(graph, color))

# Fixed node positions
pos = {
    1: (0, 0),
    2: (0, 4),
    3: (4, 4),
    4: (4, 0),
    5: (3, 2),
    6: (3, 3),
    7: (2, 3),
    8: (2, 2)
}

plt.figure(figsize=(6, 6))

# Draw edges
drawn = set()
for u in graph:
    x1, y1 = pos[u]
    for v in graph[u]:
        if (v, u) not in drawn:
            x2, y2 = pos[v]
            plt.plot([x1, x2], [y1, y2], 'k-')
            drawn.add((u, v))

# Draw nodes
for node in pos:
    x, y = pos[node]

    if color[node] == 'B':
        node_color = "skyblue"
    else:
        node_color = "yellow"

    plt.scatter(x, y, s=700, color=node_color, edgecolors='black')
    plt.text(x, y, str(node),
             ha='center', va='center',
             fontsize=12, fontweight='bold')

plt.title("Bipartite Graph")
plt.axis("off")
plt.show()
