# Program: Practice Pandas , Load Dataset, Filter Rows, Group Data, and Handle Missing Values
import pandas as pd

# Load the dataset
df = pd.read_csv("students.csv")

# Display the dataset
print("Original Dataset:")
print(df)

# Handle missing values
df["Marks"] = df["Marks"].fillna(df["Marks"].mean())

# Create a Grade column based on Marks
def assign_grade(marks):
	if marks >= 90:
		return "A"
	elif marks >= 80:
		return "B"
	elif marks >= 70:
		return "C"
	else:
		return "D"

df["Grade"] = df["Marks"].apply(assign_grade)

# Filter rows (students with marks >= 80)
print("\nStudents with Marks >= 80:")
filtered = df[df["Marks"] >= 80]
print(filtered)

# Group by Grade and calculate average marks
print("\nAverage Marks by Grade:")
grouped = df.groupby("Grade")["Marks"].mean()
print(grouped)