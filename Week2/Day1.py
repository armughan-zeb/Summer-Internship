#Creating json and csvs

import csv
import json

# ----------------- Write CSV File -----------------
data = [
    ["Name", "Age", "Marks"],
    ["Ali", 20, 85],
    ["Sara", 21, 92],
    ["Ahmed", 19, 68]
]

with open("students.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerows(data)

# ----------------- Read CSV File -----------------
print("Students with Marks >= 80 (CSV):")
with open("students.csv", "r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        if int(row["Marks"]) >= 80:
            print(row)

# ----------------- Write JSON File -----------------
students = [
    {"Name": "Ali", "Age": 20, "Marks": 85},
    {"Name": "Sara", "Age": 21, "Marks": 92},
    {"Name": "Ahmed", "Age": 19, "Marks": 68}
]

with open("students.json", "w") as file:
    json.dump(students, file, indent=4)

# ----------------- Read JSON File -----------------
print("\nStudents with Marks >= 80 (JSON):")
with open("students.json", "r") as file:
    data = json.load(file)

    for student in data:
        if student["Marks"] >= 80:
            print(student)