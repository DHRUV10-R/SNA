#— Sociograms, One-Mode and Two-Mode Networks
# Practical 6 - Sociograms, one-mode and two-mode networks
#
# Input files (keep them in the same folder as this script):
#   Emp.csv                    -> columns: Employee,Movie
#   Employee_Relationships.txt -> tab separated: person1  person2  score
#   Committee_Members.txt      -> tab separated: committee  member

import csv
import math
import matplotlib.pyplot as plt

# ---------------------------------------------------------------
# 1. Check the column names of Emp.csv
# ---------------------------------------------------------------
with open("/content/Emp.csv", "r", encoding="utf-8-sig") as file:
    reader = csv.DictReader(file)
    print(reader.fieldnames)

# ---------------------------------------------------------------
# 2. One-mode network (employee - employee, weight = common movies)
# ---------------------------------------------------------------
choices = {}
with open("/content/Emp.csv", "r", encoding="utf-8-sig") as file:
    reader = csv.DictReader(file)
    for row in reader:
        row = {k.strip().lower(): v.strip() for k, v in row.items() if k}
        employee = row["employee"]
        movie = row["movie"]
        choices.setdefault(employee, []).append(movie)

employees = list(choices.keys())

print("One-mode network:")
for i in range(len(employees)):
    for j in range(i + 1, len(employees)):
        e1 = employees[i]
        e2 = employees[j]
        common = set(choices[e1]) & set(choices[e2])
        if common:
            print(e1, "--", e2, "Weight:", len(common))

# ---------------------------------------------------------------
# 3. Two-mode network (employee -> movie)
# ---------------------------------------------------------------
employee_set = set()
movie_set = set()
edges = []
with open("/content/Emp.csv", "r", encoding="utf-8-sig") as file:
    reader = csv.DictReader(file)
    for row in reader:
        row = {k.strip().lower(): v.strip() for k, v in row.items() if k}
        employee = row["employee"]
        movie = row["movie"]
        employee_set.add(employee)
        movie_set.add(movie)
        edges.append((employee, movie))

print("Employees:", employee_set)
print("Movies:", movie_set)
print("\nTwo-mode network (Employee -> Movie):")
for employee, movie in edges:
    print(employee, "->", movie)

# ---------------------------------------------------------------
# 4. Sociogram - one-mode employee network (circular layout)
# ---------------------------------------------------------------
choices = {}
with open("/content/Emp.csv", "r", encoding="utf-8-sig") as file:
    reader = csv.DictReader(file)
    for row in reader:
        employee = row["Employee"].strip()
        movie = row["Movie"].strip()
        choices.setdefault(employee, []).append(movie)

employees = list(choices.keys())
n = len(employees)

pos = {}
for i, e in enumerate(employees):
    angle = 2 * math.pi * i / n
    pos[e] = (math.cos(angle), math.sin(angle))

for i in range(n):
    for j in range(i + 1, n):
        e1, e2 = employees[i], employees[j]
        common = set(choices[e1]) & set(choices[e2])
        if common:
            x1, y1 = pos[e1]
            x2, y2 = pos[e2]
            plt.plot([x1, x2], [y1, y2], "gray")

for e, (x, y) in pos.items():
    plt.scatter(x, y, s=700)
    plt.text(x, y, e, ha="center", va="center", color="white")

plt.title("One-Mode Employee Sociogram")
plt.axis("off")
plt.show()

# ---------------------------------------------------------------
# 5. Sociogram - two-mode employee-movie network
# ---------------------------------------------------------------
employees = list(choices.keys())
movies = sorted(set(movie for m in choices.values() for movie in m))

plt.figure(figsize=(9, 6))
pos = {}
for i, e in enumerate(employees):
    pos[e] = (0, len(employees) - i)
for i, m in enumerate(movies):
    pos[m] = (3, len(movies) - i)

for e, movie_list in choices.items():
    for m in movie_list:
        x1, y1 = pos[e]
        x2, y2 = pos[m]
        plt.plot([x1, x2], [y1, y2], color="gray")

for e in employees:
    x, y = pos[e]
    plt.scatter(x, y, s=700, color="skyblue")
    plt.text(x, y, e, ha="center", va="center")

for m in movies:
    x, y = pos[m]
    plt.scatter(x, y, s=700, color="orange")
    plt.text(x, y, m, ha="center", va="center")

plt.title("Two-Mode Employee-Movie Sociogram")
plt.axis("off")
plt.show()

# ---------------------------------------------------------------
# 6. Persons-by-persons sociogram (green = +ve, red = -ve, grey = 0)
# ---------------------------------------------------------------
relationships = {}
with open("/content/Employee_Relationships.txt", "r") as file:
    reader = csv.reader(file, delimiter="\t")
    for row in reader:
        if len(row) >= 3:
            a = row[0].strip()
            b = row[1].strip()
            score = float(row[2])
            relationships[(a, b)] = score

people = sorted(set(p for pair in relationships for p in pair))
n = len(people)

pos = {}
for i, p in enumerate(people):
    angle = 2 * math.pi * i / n
    pos[p] = (math.cos(angle), math.sin(angle))

plt.figure(figsize=(8, 8))
for (a, b), score in relationships.items():
    x1, y1 = pos[a]
    x2, y2 = pos[b]
    color = "green" if score > 0 else "red" if score < 0 else "gray"
    plt.plot([x1, x2], [y1, y2], color=color,
             linewidth=max(0.5, abs(score) / 30))

for p, (x, y) in pos.items():
    plt.scatter(x, y, s=700, color="skyblue")
    plt.text(x, y, p, ha="center", va="center")

plt.title("Persons-by-Persons Sociogram")
plt.axis("off")
plt.show()

# ---------------------------------------------------------------
# 7. Committee-by-committee sociogram
# ---------------------------------------------------------------
committees = {}
with open("/content/Committee_Members.txt", "r") as file:
    reader = csv.reader(file, delimiter="\t")
    for row in reader:
        if len(row) >= 2:
            c = row[0].strip()
            e = row[1].strip()
            committees.setdefault(c, set()).add(e)

names = list(committees.keys())
n = len(names)

pos = {}
for i, c in enumerate(names):
    angle = 2 * math.pi * i / n
    pos[c] = (math.cos(angle), math.sin(angle))

plt.figure(figsize=(7, 7))
for i in range(n):
    for j in range(i + 1, n):
        c1, c2 = names[i], names[j]
        common = committees[c1] & committees[c2]
        if common:
            x1, y1 = pos[c1]
            x2, y2 = pos[c2]
            plt.plot([x1, x2], [y1, y2], color="gray", linewidth=len(common))

for c, (x, y) in pos.items():
    plt.scatter(x, y, s=900, color="orange")
    plt.text(x, y, c, ha="center", va="center")

plt.title("Committee-by-Committee Sociogram")
plt.axis("off")
plt.show()

print("Shared committee members:")
for i in range(n):
    for j in range(i + 1, n):
        c1, c2 = names[i], names[j]
        common = committees[c1] & committees[c2]
        if common:
            print(c1, c2, "Weight:", len(common))

            