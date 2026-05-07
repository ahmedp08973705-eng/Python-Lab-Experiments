import numpy as np
import pandas as pd
# NumPy Example
arr = np.array([10, 20, 30, 40, 50])

print("NumPy Array:")
print(arr)

print("Array Mean:", np.mean(arr))
print("Array Sum:", np.sum(arr))

# Pandas Example

data = {
    "Name": ["John", "Alice", "David"],
    "Marks": [85, 90, 78]
}


df = pd.DataFrame(data)

print("\nPandas DataFrame:")
print(df) 


