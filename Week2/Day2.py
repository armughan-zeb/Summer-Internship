#Practicing numpy

import numpy as np

# Create an array
arr = np.array([10, 20, 30, 40, 50, 60])

# Indexing
print("First element:", arr[0])
print("Last element:", arr[-1])

# Slicing
print("First three elements:", arr[:3])
print("Last three elements:", arr[3:])

# Basic Statistics
print("Sum:", np.sum(arr))
print("Mean:", np.mean(arr))
print("Maximum:", np.max(arr))
print("Minimum:", np.min(arr))
print("Standard Deviation:", np.std(arr))