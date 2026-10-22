import numpy as np
import matplotlib.pyplot as plt
# adjacency matrix representation of a graph
nodes1 = ["A", "B", "C", "D"]

adj_matrix1 = np.array([
    [0, 1, 0, 1],
    [1, 0, 1, 1],
    [0, 1, 0, 1],
    [1, 1, 1, 0]
])

print("Nodes:", nodes1)
print(adj_matrix1)
#using edge list representation of a graph
def create_adjacency_matrix(V, edges):

    matrix = [[0] * V for _ in range(V)]

    for edge in edges:
        u, v = edge
        matrix[u][v] = 1
        matrix[v][u] = 1

    return matrix


V2 = 4
edges2 = [(0, 1), (1, 2), (1, 3), (2, 3), (3, 0)]
adj_matrix2 = create_adjacency_matrix(V2, edges2)

print("ROWS: ")
for row in adj_matrix2:
    print(row)

#using Sociogram representation of a graph
import numpy as np
import matplotlib.pyplot as plt


matrix = np.array([
    [1, 1, 0, 1],
    [1, 0, 1, 0],
    [0, 0, 0, 1],
    [1, 1, 1, 0],
    [0, 0, 0, 1]
])


node_positions = {
    "A": [2, 0],
    "B": [1, 2],
    "C": [0, 3],
    "D": [1, 1],
    "E": [3, 0]
}


nodes = ["A", "B", "C", "D", "E"]



for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        if matrix[i][j] == 1:
            plt.plot(
                [node_positions[nodes[i]][0], node_positions[nodes[j]][0]],
                [node_positions[nodes[i]][1], node_positions[nodes[j]][1]],
                color='red'
            )


for node in nodes:
    x, y = node_positions[node]


    plt.scatter(x, y, color='blue', marker='s', s=500)


    plt.text(x, y, node, fontsize=12, color='white',
             ha='center', va='center')

print(matrix)
print(node_positions)
print(nodes)
plt.title("Sociogram")
plt.axis('equal')
plt.axis('off')
plt.show()