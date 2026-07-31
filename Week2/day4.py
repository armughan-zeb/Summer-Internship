# Program: Merge Two DataFrames and Produce a Summary

import pandas as pd

# Create the first dataset
students = {
    "ID": [1, 2, 3],
    "Name": ["Ali", "Sara", "Ahmed"]
}

# Create the second dataset
marks = {
    "ID": [1, 2, 3],
    "Marks": [85, 92, 78]
}

# Convert dictionaries into DataFrames
df1 = pd.DataFrame(students)
df2 = pd.DataFrame(marks)

# Merge the DataFrames
merged = pd.merge(df1, df2, on="ID")

# Display the merged dataset
print("Merged DataFrame:")
print(merged)

# Produce a summary
print("\nSummary:")
print("Total Students:", len(merged))
print("Average Marks:", merged["Marks"].mean())
print("Highest Marks:", merged["Marks"].max())
print("Lowest Marks:", merged["Marks"].min())