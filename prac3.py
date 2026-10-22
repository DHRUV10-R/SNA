import numpy as np
import pandas as pd


df = pd.read_csv('/content/Student_relation.csv', index_col=0)

print("Adjacency Matrix:\n")
print(df)

A = df.values
labels = df.index.tolist()

print(A)
# Degree Matrix

degree_values = np.sum(A, axis=1)
D = np.diag(degree_values)

print("\nDegree Matrix:")
print(D)


# Laplacian Matrix
L = D - A

print("\nLaplacian Matrix:")
print(L)


# Transition Probability Matrix
P = np.divide(
    A,
    degree_values[:, np.newaxis],
    out=np.zeros_like(A, dtype=float),
    where=degree_values[:, np.newaxis] != 0
)

print("\nTransition Probability Matrix:")
print(P)


# Edge List (Undirected Graph)
edges = []

for i in range(len(labels)):
    for j in range(i + 1, len(labels)):
        if A[i, j] == 1:
            edges.append((i, j))

print("\nEdges:")
for edge in edges:
    print((labels[edge[0]], labels[edge[1]]))

# Incidence Matrix
I = np.zeros((len(labels), len(edges)), dtype=int)

for k, (u, v) in enumerate(edges):
    I[u, k] = 1
    I[v, k] = 1

print("Incidence Matrix:\n", I)

# Incidence Matrix setup
edges = []
for i in range(len(labels)):
    for j in range(len(labels)):
        if A[i][j] == 1:
            edges.append((i, j))

I = np.zeros((len(labels), len(edges)), dtype=int)
for k, (u, v) in enumerate(edges):
    I[u][k] = -1
    I[v][k] = 1
print("Incidence Matrix:\n", I)

# TWO-MODE DATA REPRESENTATION
# Student-Course Network

import numpy as np
import pandas as pd

df = pd.read_csv('/content/student_subject_preferences.csv', index_col=0)

print("Two-Mode Matrix:")
print(df)

B = df.values
students = df.index.tolist()
courses = df.columns.tolist()
#Student Degree
student_degree = np.sum(B, axis=1)

print("\nStudent Degree:")
for i in range(len(students)):
    print(students[i], "=", student_degree[i])

#Course Degree
course_degree = np.sum(B, axis=0)

print("\nCourse Degree:")
for i in range(len(courses)):
    print(courses[i], "=", course_degree[i])
#Edge List
edges = []

for i in range(len(students)):
    for j in range(len(courses)):
        if B[i, j] == 1:
            edges.append((students[i], courses[j]))

print("\nEdges:")
for student, course in edges:
    print(student, "-", course)

#Incidence Matrix
I = B.copy()

print("\nIncidence Matrix:")
print(pd.DataFrame(I, index=students, columns=courses))
# 5. Adjacency Matrix
# Create bipartite adjacency matrix:
# [ 0   B ]
# [ Bᵀ  0 ]

A = np.block([
    [
        np.zeros(
            (len(students), len(students)),
            dtype=int
        ),
        B
    ],
    [
        B.T,
        np.zeros(
            (len(courses), len(courses)),
            dtype=int
        )
    ]
])

nodes = students + courses

print("\nAdjacency Matrix:")
print(pd.DataFrame(A, index=nodes, columns=nodes))

#Degree Diagonal Matrix
degree = np.sum(A, axis=1)

D = np.diag(degree)

print("\nDegree Diagonal Matrix:")
print(pd.DataFrame(D, index=nodes, columns=nodes))
#Laplacian Matrix
L = D - A

print("\nLaplacian Matrix:")
print(pd.DataFrame(L, index=nodes, columns=nodes))

# Transition Probability Matrix
P = np.divide(
    A,
    degree[:, np.newaxis],
    out=np.zeros_like(A, dtype=float),
    where=degree[:, np.newaxis] != 0
)

print("\nTransition Probability Matrix:")
print(pd.DataFrame(P, index=nodes, columns=nodes))

#Incidence Matrix of Complete Bipartite Network

I_full = np.zeros(
    (len(nodes), len(edges)),
    dtype=int
)

for k, (student, course) in enumerate(edges):
    I_full[students.index(student), k] = 1
    I_full[
        len(students) + courses.index(course), k
    ] = 1

print("\nFull Incidence Matrix:")
print(
    pd.DataFrame(
        I_full,
        index=nodes,
        columns=[f"E{i+1}" for i in range(len(edges))]
    )
)