# Practical 8 - Weighted projection of a two-mode network

# Needs Emp.csv (columns: Employee,Movie) in the same folder.
# (In the original notebook `choices` came from Practical 6; it is
#  rebuilt here so this file runs on its own.)

import csv

choices = {}
with open("Emp.csv", "r", encoding="utf-8-sig") as file:
    reader = csv.DictReader(file)
    for row in reader:
        row = {k.strip().lower(): v.strip() for k, v in row.items() if k}
        choices.setdefault(row["employee"], []).append(row["movie"])

# ---------------------------------------------------------------
# Weighted projection: weight = number of movies two employees share
# ---------------------------------------------------------------
employees = list(choices.keys())
projection = {}

for i in range(len(employees)):
    for j in range(i + 1, len(employees)):
        e1 = employees[i]
        e2 = employees[j]
        common = set(choices[e1]) & set(choices[e2])
        if len(common) > 0:
            projection[(e1, e2)] = len(common)

print("Weighted Projection:")
for pair, weight in projection.items():
    print(pair[0], "-", pair[1], ":", weight)